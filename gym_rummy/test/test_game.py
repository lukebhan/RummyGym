"""Tests the functionality of the game"""

import unittest
import sys
import numpy as np
import gym
import gym_rummy #pylint: disable=W0611
sys.path.append('./envs')

class TestGame(unittest.TestCase):
    """Testing the game class"""

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
        finish = False
        count = 0
        while not finish:
            _, _, finish, _ = env.step(np.random.rand(2))
            self.assertEqual(obs[8], 7)
            count += 1

    def test_monte_carlo(self):
        """Test the monte carlo sims"""
        env=gym.make('Rummy-v0', verbose=False)
        player1 = 0
        player2 = 0
        length = []
        for _ in range(100):
            obs = env.reset()
            # Draw from pile and discard last card
            finish = False
            count = 0
            while not finish:
                _, _, finish, info = env.step(np.random.rand(2))
                self.assertEqual(obs[8], 7)
                count += 1
            if info["p1score"] > info["p2score"]:
                player1 += 1
            else:
                player2 += 1
            length.append(count)
        print("Final Win Counts")
        print("P1", str(player1))
        print("P2", str(player2))
        print("Avg Length", np.mean(length))
