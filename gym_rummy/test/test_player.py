"""A class to test the player class"""

import unittest
#import numpy as np

import sys
sys.path.append("./envs")
from player import Player #pylint: disable=E0401,C0413
from deck import Deck #pylint: disable=E0401,C0413

class TestPlayer(unittest.TestCase):
    """Testing the player class"""

    def test_draw_card(self):
        """Check that draw_card works"""
        player1= Player({})
        draw_pile = Deck()
        player1.draw_card(draw_pile)
        self.assertEqual(len(draw_pile), 51)
        self.assertEqual(len(player1.get_hand()), 1)
        for i in range(1, 51):
            player1.draw_card(draw_pile)
            self.assertEqual(len(draw_pile), 51-i)

    def test_pickup_pile(self):
        """Check that pickup_pile works"""
        player1 = Player({})
        draw_pile = Deck()
        player1.pickup_pile(draw_pile)
        self.assertEqual(len(draw_pile), 26)
        self.assertEqual(len(player1.get_hand()), 26)
        player1.pickup_pile(draw_pile)
        self.assertEqual(len(draw_pile), 13)
        self.assertEqual(len(player1.get_hand()), 39)
        player1.pickup_pile(draw_pile)
        self.assertEqual(len(draw_pile), 7)
        self.assertEqual(len(player1.get_hand()), 45)
        player1.pickup_pile(draw_pile)
        self.assertEqual(len(draw_pile), 4)
        self.assertEqual(len(player1.get_hand()), 48)
        player1.pickup_pile(draw_pile)
        self.assertEqual(len(draw_pile), 2)
        self.assertEqual(len(player1.get_hand()), 50)
        player1.pickup_pile(draw_pile)
        self.assertEqual(len(draw_pile), 1)
        self.assertEqual(len(player1.get_hand()), 51)
        player1.pickup_pile(draw_pile)
        self.assertEqual(len(draw_pile), 0)
        self.assertEqual(len(player1.get_hand()), 52)

    def test_discard(self):
        """Check that discarding works"""
        discard_deck  =Deck()
        discard_deck.empty_deck()
        player1 = Player(None)
        #self.assertRaises(IndexError, p1.discard, 52, discardDeck)
        player1.discard(51, discard_deck)
        self.assertEqual(len(discard_deck), 1)
        self.assertEqual(len(player1.get_hand()), 51)
        player1.discard(50, discard_deck)

        self.assertEqual(len(player1.get_hand()), 50)

        self.assertEqual(len(discard_deck), 2)

        player1.discard(0, discard_deck)

        self.assertEqual(len(player1.get_hand()), 49)

        self.assertEqual(len(discard_deck), 3)
        ordered_discards = {"ADiamonds": 1, "KDiamonds": 1, "2Hearts":1}
        self.assertEqual(discard_deck, Deck(ordered_discards))
        ordered_discards = ["ADiamonds", "KDiamonds", "2Hearts"]
        for idx, card in enumerate(discard_deck):
            self.assertEqual(ordered_discards[idx], card)

    def test_place_sets(self):
        """Check that getting sets works"""
        player1 = Player(None)
        player1.place_sets()
        # Max score is 396
        self.assertEqual(396, player1.get_score())
        self.assertEqual(len(player1.get_hand()), 0)
        # Test 3 aces
        player1 = Player({"ADiamonds":1, "AClubs": 1, "ASpades": 1})
        player1.place_sets()
        self.assertEqual(45, player1.get_score())

        self.assertEqual(len(player1.get_hand()), 0)
        self.assertEqual(len(player1.get_hand()), 0)

        # test run
        player1 = Player({"2Clubs": 1, "3Clubs": 1, "4Clubs": 1, "5Hearts": 1})
        player1.place_sets()
        self.assertEqual(9, player1.get_score())
        self.assertEqual(len(player1.get_hand()), 1)

if __name__ == '__main__':
    unittest.main()
