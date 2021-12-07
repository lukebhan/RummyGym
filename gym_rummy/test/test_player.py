import unittest
import numpy as np

import sys
sys.path.append("./envs")
from player import Player
from deck import Deck

class TestPlayer(unittest.TestCase):
    def testDrawCard(self):
        p1= Player({})
        drawPile = Deck()
        p1.drawCard(drawPile)
        self.assertEqual(len(drawPile), 51)
        self.assertEqual(len(p1.getHand()), 1)
        for i in range(1, 51):
            p1.drawCard(drawPile)
            self.assertEqual(len(drawPile), 51-i)

    def testPickupPile(self):
        p1 = Player({})
        drawPile = Deck()
        p1.pickupPile(drawPile)
        self.assertEqual(len(drawPile), 26)
        self.assertEqual(len(p1.getHand()), 26)
        p1.pickupPile(drawPile)
        self.assertEqual(len(drawPile), 13)
        self.assertEqual(len(p1.getHand()), 39)
        p1.pickupPile(drawPile)
        self.assertEqual(len(drawPile), 7)
        self.assertEqual(len(p1.getHand()), 45)
        p1.pickupPile(drawPile)
        self.assertEqual(len(drawPile), 4)
        self.assertEqual(len(p1.getHand()), 48)
        p1.pickupPile(drawPile)
        self.assertEqual(len(drawPile), 2)
        self.assertEqual(len(p1.getHand()), 50)
        p1.pickupPile(drawPile)
        self.assertEqual(len(drawPile), 1)
        self.assertEqual(len(p1.getHand()), 51)
        p1.pickupPile(drawPile)
        self.assertEqual(len(drawPile), 0)
        self.assertEqual(len(p1.getHand()), 52)

    def testDiscard(self):
        discardDeck  =Deck()
        discardDeck.emptyDeck()
        p1 = Player(None)
        self.assertRaises(IndexError, p1.discard, 52, discardDeck) 
        p1.discard(51, discardDeck)
        self.assertEqual(len(discardDeck), 1)
        self.assertEqual(len(p1.getHand()), 51)
        p1.discard(50, discardDeck)

        self.assertEqual(len(p1.getHand()), 50)

        self.assertEqual(len(discardDeck), 2)

        p1.discard(0, discardDeck)

        self.assertEqual(len(p1.getHand()), 49)

        self.assertEqual(len(discardDeck), 3)
        orderedDiscards = {"ADiamonds": 1, "KDiamonds": 1, "2Hearts":1}
        self.assertEqual(discardDeck, Deck(orderedDiscards))
        orderedDiscards = ["ADiamonds", "KDiamonds", "2Hearts"]
        for idx, card in enumerate(discardDeck):
            self.assertEqual(orderedDiscards[idx], card)

    def testPlaceSets(self):
        p1 = Player(None)
        p1.placeSets()
        # Max score is 396
        self.assertEqual(396, p1.getScore())
        self.assertEqual(len(p1.getHand()), 0)
        # Test 3 aces
        p1 = Player({"ADiamonds":1, "AClubs": 1, "ASpades": 1})
        p1.placeSets()
        self.assertEqual(45, p1.getScore())

        self.assertEqual(len(p1.getHand()), 0)
        self.assertEqual(len(p1.getHand()), 0)

        # test run
        p1 = Player({"2Clubs": 1, "3Clubs": 1, "4Clubs": 1, "5Hearts": 1})
        p1.placeSets()
        self.assertEqual(9, p1.getScore())
        self.assertEqual(len(p1.getHand()), 1)

if __name__ == '__main__':
    unittest.main()
