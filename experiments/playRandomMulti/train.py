import sys
sys.path.append('../../gym_rummy/envs')

import gym
import os
import numpy as np
import gym_rummy
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.results_plotter import load_results, ts2xy, plot_results
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

env = gym.make("Rummy-v0", verbose=False)

log_dir = "PPOMulti3/"
os.makedirs(log_dir, exist_ok=True)

env=Monitor(env, log_dir)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(250000)
model.save('modelMulti3')

# Evaluate the agent
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

print(mean_reward, std_reward)

obs = env.reset()
p1Count = 0
p2Count = 0
tie = 0
for i in range(1000):
    obs = env.reset()
    terminate = False
    while not terminate:
        action = model.predict(obs)
        obs, reward, terminate, info = env.step(action[0])
    if info["win"]:
        p1Count += 1
    else:
        p2Count += 1

print("Wins:",p1Count)
print("Loses:", p2Count)
