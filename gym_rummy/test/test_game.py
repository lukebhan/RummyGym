import sys
sys.path.append('./envs')

import unittest
import gym 
import gym_rummy
import numpy as np

class TestGame(unittest.TestCase):
    def test_initialize(self):
        """ Make sure reset is working """
        env=gym.make('Rummy-v0', verbose=False)
        obs = env.reset()
        self.assertEqual(obs[8], 7)
        self.assertEqual(obs[9], 7)
        self.assertEqual(obs[10], 0)

    def test_first_step(self):
        """ Test first step of the game with known actions """
        env=gym.make('Rummy-v0', verbose=False)
        obs = env.reset()
        # Draw from pile and discard last card
        finish = False;
        count = 0
        while not finish:
            nextState, rew, finish, info = env.step(np.random.rand(2))
            self.assertEqual(obs[8], 7)
            count += 1

    def test_monte_carlo(self):
        env=gym.make('Rummy-v0', verbose=False)
        p1 = 0
        p2 = 0
        length = []
        for i in range(100):
            obs = env.reset()
            # Draw from pile and discard last card
            finish = False;
            count = 0
            while not finish:
                nextState, rew, finish, info = env.step(np.random.rand(2))
                self.assertEqual(obs[8], 7)
                count += 1
            if info["p1score"] > info["p2score"]:
                p1 += 1
            else:
                p2 += 1
            length.append(count)
        print("Final Win Counts")
        print("P1", str(p1))
        print("P2", str(p2))
        print("Avg Length", np.mean(length))
