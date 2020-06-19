cd "D:\Projects\DTU DRL Special Course\DRLPython\NG"

python a2c_main.py ^
-env="Flight" ^
-dimensionStatePolicy=15 ^
-dimensionStateCritic=15 ^
-dimensionActionPolicy=3 ^
-iterations=10000 ^
-num_workers=4 ^
-nstep=100 ^
-rolloutlimit=5000 ^
-discount=0.995 ^
-lr_policy=1e-4 ^
-lr_policy_gamma=0.4642 ^
-lr_policy_stepsize=40001 ^
-policy_weight_decay=1e-7 ^
-continuous_sigma=0.3 ^
-continuous_sigma_end=0.2 ^
-continuous_sigma_steps=10000 ^
-lr_critic=1e-3 ^
-lr_critic_gamma=0.4642 ^
-lr_critic_stepsize=40001 ^
-val_count=100 ^
-val_sample_size=10 ^
-actionFrequency=10 ^
-difficulty=1.00 ^
-windPower=2.5 ^
-windAngleDeviation=25.0 ^
-path_policy="D:\Projects\DTU DRL Special Course\Results\2020-06-17 22-27-06 Flight\net_policy_final.pt" ^
-path_critic="D:\Projects\DTU DRL Special Course\Results\2020-06-17 22-27-06 Flight\net_critic_final.pt"
pause