"""Creates the rummy environment"""

import sys
import pathlib
import gym
from gym import spaces
import torch
import numpy as np
sys.path.append('./envs')

from player import Player #pylint: disable=C0413, E0401
from deck import Deck #pylint: disable=C0413, E0401
from .encoder.autoencoder import AE #pylint: disable=E0402, C0413,E0401
#from hand import Hand

class RummyEnv(gym.Env): #pylint: disable=W0223, R0902
    """Rummy environment"""

    def __init__(self):
        """Initialized the rummy environment"""
        super(RummyEnv, self).__init__() #pylint: disable=R1725
        self.verbose = False

        # Set spaces
        self.action_space = spaces.Box(np.full(2, 0, \
        dtype=np.float32), np.full(2, 1, dtype=np.float32))
        self.observation_space = spaces.Box(np.full(11, 0, \
        dtype=np.float32), np.full(11, 1, dtype=np.float32))

        # Create autoencoder. Use relative path
        self.ae = AE() # pylint: disable=C0103
        # We load our current path of this file
        path = pathlib.Path(__file__).parent.resolve()
        self.ae.load_state_dict(torch.load(str(path) + '/encoder/ae.pt'))
        self.ae.eval()

        # Initialize to None
        self.player1 = None
        self.player2 = None
        self.state = None
        self.rew = None
        self.draw_deck = None
        self.discard_deck = None

    def reset(self):
        """ Create our initial decks"""
        self.draw_deck = Deck()
        self.discard_deck = Deck()
        self.discard_deck.empty_deck()

        # Create our two players. Each starts with 7 cards
        self.player1 = Player({}, "Player 1", self.verbose)
        self.player2 = Player({}, "Player 2", self.verbose)
        for _ in range(7):
            self.player1.draw_card(self.draw_deck)
            self.player2.draw_card(self.draw_deck)

        # Build state space. Villan will be player2 in this case
        with torch.no_grad():
            tensor = torch.from_numpy(\
            self.player1.get_hand().to_numpy().reshape((1, 52))).float() #pylint: disable=E1101
            reduced_dim = self.ae.encode(tensor).numpy().reshape(8)
            self.state = np.concatenate([reduced_dim, \
            [len(self.player1.get_hand())], \
            [len(self.player2.get_hand())],\
            [len(self.discard_deck)]])
        return self.state

    def step(self, action):
        """Take one step or turn in the game"""
        self.player1.take_turn(action, self.draw_deck, self.discard_deck)
        # Let player2 take random actions
        action_two = np.random.rand(2)
        self.player2.take_turn(action_two, self.draw_deck, \
        self.discard_deck)
        with torch.no_grad():
            tensor = torch.from_numpy(\
            self.player1.get_hand().to_numpy().reshape((1, 52))).float() #pylint: disable=E1101
            reduced_dim = self.ae.encode(tensor).numpy().reshape(8)
            self.state = np.concatenate([reduced_dim, \
            [len(self.player1.get_hand())], \
            [len(self.player2.get_hand())],\
            [len(self.discard_deck)]])
            # updates self.rew var
            self.reward()
            finish = self.terminate()
        return  self.state, \
                self.rew, \
                finish, \
                {"p1score": self.player1.get_score(), \
                "p2score": self.player2.get_score()}

    def terminate(self):
        """End the game if a player has no cards left or if the deck is empty"""
        if len(self.player1.get_hand()) == 0 \
        or len(self.player2.get_hand()) == 0 or \
        len(self.draw_deck) == 0:
            if self.verbose:
<<<<<<< HEAD
                print("Game ended:")
                print("Player 1 had: ",len(self.player1.get_hand())," cards")
                print("Player 2 had: ",len(self.player2.get_hand())," cards")
                if (self.player1.get_score()) > (self.player2.get_score()):
                    self.rew+= 10
=======
                print("Game ended:") 
                print("Player 1 had: ",len(self.p1.getHand())," cards")
                print("Player 2 had: ",len(self.p2.getHand())," cards")
            if (self.p1.getScore()) > (self.p2.getScore()):
                self.rew += 50
>>>>>>> 1a029afe4794065a913d0d4ec60d209c6ded0db3
            return True
        return False

    def reward(self):
<<<<<<< HEAD
        """Reward function"""
        if self.player1.get_score() > self.player2.get_score():
            self.rew =(self.player1.get_score()-self.player2.get_score() )/ 396
        else:
=======
        if self.p1.getScore() > self.p2.getScore():
            self.rew =(self.p1.getScore()-self.p2.getScore())/ 396
        else: 
>>>>>>> 1a029afe4794065a913d0d4ec60d209c6ded0db3
            self.rew = 0
