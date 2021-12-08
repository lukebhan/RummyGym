import sys
sys.path.append('../../gym_rummy/envs')

import gym
import os
import numpy as np
import gym_rummy
from stable_baselines3 import SAC

env = gym.make('Rummy-v0', verbose=False)
model = SAC("MlpPolicy", env)
model.load('tmp/best_model1')

p1count = 0
p2count = 0
tie = 0
for i in range(10000):
    obs = env.reset()
    terminate = False
    while not terminate:
        action = model.predict(obs)
        obs, reward, terminate, info = env.step(action[0])
    if info["p1score"] > info["p2score"]:
        p1count += 1
    elif info["p1score"] == info["p2score"]:
        tie += 1
    else:
        p2count += 1
print("After 1000 games, our agent performed in the following")
print("Win:", p1count, "Lose:", p2count, "Tie:", tie)

