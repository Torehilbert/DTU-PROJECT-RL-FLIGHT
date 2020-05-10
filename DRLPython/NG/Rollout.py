import random
import torch

#from BoxPreprocessor import preprocess_state, preprocess_action
import BoxPreprocessor


class RolloutGenerator():
    def __init__(self, net, env, episode_steps_max=500):
        self.net = net
        self.env = env
        self.episode_steps_max = episode_steps_max
        self.step_current = 0

    def initialize(self):
        self.state = self.env.initial_state()

    def close(self):
        self.env.close()

    @staticmethod
    def sample_action(probs):
        roll = random.random()
        prob_cumsum = probs.cumsum(dim=0)
        action = len(probs) - 1
        for j in range(len(probs) - 1):
            if roll <= prob_cumsum[j]:
                action = j
                break
        return action

    def generate_rollout(self, n_steps, action_mode, auto_reset=False):
        states = []
        actions = []
        logprobs = []
        rewards = []

        for i in range(n_steps):
            self.state = BoxPreprocessor.preprocess_state(self.state)
            states.append(self.state)

            # get action
            action, logprob = self.net.action(self.state, action_mode=action_mode)
            actions.append(action)

            # take step
            status, state_next, reward, done = self.env.step(0, action, "")
            self.state = state_next

            # save
            rewards.append(reward)
            logprobs.append(logprob)

            if done:
                break

        states.append(BoxPreprocessor.preprocess_state(self.state))

        if done or auto_reset:
            self.state = self.env.reset()

        states = torch.stack((states))
        logprobs = torch.stack((logprobs))
        return states, rewards, logprobs, status, done


def calculate_returns(rewards, discount, normalize=False, terminal_value=0):
    returns = [0] * len(rewards)

    R = terminal_value
    for i in reversed(range(len(rewards))):
        R = rewards[i] + discount * R
        returns[i] = R

    returns = torch.tensor(returns)
    if normalize:
        returns = (returns - returns.mean()) / (returns.std() + 1e-10)
    return returns
