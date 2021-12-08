"""Generates decks for our environment"""

import sys
import numpy as np
sys.path.append("./envs")
#from deck import Deck #pylint: disable=E0401,C0413

def generate_inst(prob):
    """Generates an instance of what cards we have"""
    arr = np.zeros(52)
    for i in range(52):
        if np.random.rand() < prob:
            arr[i] = 1
    return arr

# We will use 1000 from 19 (0.5 -> 0.95) different distributions for 19k points
DIST = 0
data = []
for _ in range(19):
    DIST += 0.05
    for _ in range(1000):
        data.append(generate_inst(DIST))
np.savetxt('deckdata.txt', data)
