import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
import numpy as np

rewards= []
rewards2 = []
rewards3 = []
avgReward = []
avgReward2 = []
avgReward3 = []
boundTop = []
boundBottom = []
plotMean = []
f2 = open('PPOMulti1/monitor.csv', 'r')
f3 = open('PPOMulti2/monitor.csv', 'r')
with open('PPOMulti3/monitor.csv') as f:
    f.readline()
    f.readline()
    f2.readline()
    f2.readline()
    f3.readline()
    f3.readline()
    line = f.readline()
    line2 = f2.readline()
    line3 = f3.readline()
    while line and line2 and line3:
        arr = line.split(",")
        arr2 = line2.split(",")
        arr3 = line3.split(",")
        rewards.append(float(arr[0]))
        rewards2.append(float(arr2[0]))
        rewards3.append(float(arr3[0]))
        avgReward.append(np.mean(rewards[-20:]))
        avgReward2.append(np.mean(rewards2[-20:]))
        avgReward3.append(np.mean(rewards3[-20:]))
        plotMean.append(np.mean([avgReward[-1], avgReward2[-1], avgReward3[-1]]))
        boundBottom.append(min(avgReward[-1], avgReward2[-1], avgReward3[-1]))
        boundTop.append(np.amax([avgReward[-1], avgReward2[-1], avgReward3[-1]]))
        line = f.readline()
        line2 = f.readline()
        line3 = f.readline()
fig, ax = plt.subplots()
print(plotMean[0], boundBottom[0])
x = np.linspace(0, len(plotMean), len(plotMean))
ax.plot(x, plotMean, color="orange")
ax.fill_between(x, boundBottom, boundTop, color='blue', alpha=.3)
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Training Rewards")
plt.savefig('reward1.png')
plt.show()
