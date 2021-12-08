import numpy as np 
from deck import Deck

def generateInst(p):
    arr = np.zeros(52)
    for i in range(52):
        if np.random.rand() < p:
            arr[i] = 1
    return arr

# We will use 1000 from 19 (0.5 -> 0.95) different distributions for 19k points
dist = 0
data = []
for i in range(19):
    dist += 0.05
    for j in range(1000):
        data.append(generateInst(dist))
np.savetxt('deckdata.txt', data)
