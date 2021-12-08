import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
import numpy as np

rewards= []
avgReward = []
with open('tmp/monitor.csv') as f:
    f.readline()
    f.readline()
    line = f.readline()
    while line:
        arr = line.split(",")
        rewards.append(float(arr[0]))
        avgReward.append(np.mean(rewards[-20:]))
        line = f.readline()
plt.figure()
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.plot(rewards)
plt.plot(avgReward, label="Averge Last 5 Epsiodes")
plt.show()

