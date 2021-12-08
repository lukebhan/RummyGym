import gym
from gym import spaces
import torch
import numpy as np
import pathlib
import sys
sys.path.append('./envs')

from .encoder.autoencoder import AE
from deck import Deck
from player import Player
from hand import Hand

class RummyEnv(gym.Env):
    def __init__(self, verbose):
        super(RummyEnv, self).__init__()
        self.verbose = verbose

        # Set spaces
        self.action_space = spaces.Box(np.full(2, 0, dtype=np.float32), np.full(2, 1, dtype=np.float32))
        self.observation_space = spaces.Box(np.full(11, 0, dtype=np.float32), np.full(11, 1, dtype=np.float32))

        # Create autoencoder. Use relative path
        self.ae = AE()
        # We load our current path of this file 
        path = pathlib.Path(__file__).parent.resolve()
        self.ae.load_state_dict(torch.load(str(path) + '/encoder/ae.pt'))
        self.ae.eval()

    def reset(self):
        # Create our initial decks
        self.drawDeck = Deck()
        self.discardDeck = Deck()
        self.discardDeck.emptyDeck()

        # Create our two players. Each starts with 7 cards
        # for a 4 player case, use 5 cards
        self.p1 = Player({}, "Player 1", self.verbose)
        self.p2 = Player({}, "Player 2", self.verbose)
        self.p3 = Player({}, "Player 2", self.verbose)
        self.p4 = Player({}, "Player 2", self.verbose)
        for i in range(5):
            self.p1.drawCard(self.drawDeck)
            self.p2.drawCard(self.drawDeck)
            self.p3.drawCard(self.drawDeck)
            self.p4.drawCard(self.drawDeck)

        # set win to be false initially
        self.win = False

        # Build state space. Villan will be player2 in this case
        with torch.no_grad():
            tensor = torch.from_numpy(self.p1.getHand().toNumpy().reshape((1, 52))).float()
            reducedDim = self.ae.encode(tensor).numpy().reshape(8)
            self.state = np.concatenate([reducedDim, [len(self.p1.getHand())], [len(self.p2.getHand())],[len(self.discardDeck)]])
        return self.state

    def step(self, action):
        self.p1.takeTurn(action, self.drawDeck, self.discardDeck)
        # Let player2 take random actions
        action_two = np.random.rand(2)
        action_three = np.random.rand(2)
        action_four = np.random.rand(2)
        self.p2.takeTurn(action_two, self.drawDeck, self.discardDeck)
        self.p3.takeTurn(action_three, self.drawDeck, self.discardDeck)
        self.p4.takeTurn(action_four, self.drawDeck, self.discardDeck)
        with torch.no_grad():
            tensor = torch.from_numpy(self.p1.getHand().toNumpy().reshape((1, 52))).float()
            reducedDim = self.ae.encode(tensor).numpy().reshape(8)
            self.state = np.concatenate([reducedDim, [len(self.p1.getHand())], [len(self.p2.getHand())],[len(self.discardDeck)]])
            # updates self.rew var
            self.reward()
            finish = self.terminate()
        return self.state, self.rew, finish, {"win": self.win}

    def terminate(self):
        if len(self.p1.getHand()) == 0 or len(self.p2.getHand()) == 0 or len(self.p3.getHand()) == 0 or len(self.p4.getHand()) == 0 or len(self.drawDeck) == 0:
            if self.verbose:
                print("Game ended:") 
                print("Player 1 had: ",len(self.p1.getHand())," cards")
                print("Player 2 had: ",len(self.p2.getHand())," cards")
            if (self.p1.getScore()) > (self.p2.getScore()) and (self.p1.getScore()) > (self.p3.getScore()) and (self.p1.getScore()) > self.p4.getScore():
                self.win = True
                self.rew += 50
            else:
                self.win=False
            return True
        else: 
            return False

    def reward(self):
        if (self.p1.getScore()) > (self.p2.getScore()) and (self.p1.getScore()) > (self.p3.getScore()) and (self.p1.getScore()) > self.p4.getScore():
            self.rew =(self.p1.getScore()-max(self.p2.getScore(), self.p3.getScore(), self.p4.getScore()))/ 396
        else: 
            self.rew = 0
