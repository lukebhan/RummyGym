"""A unit testing framework for the hand class"""
import unittest
import sys
sys.path.append("./envs")
from deck import Deck #pylint: disable=E0401,C0413
from hand import Hand #pylint: disable=E0401,C0413

class TestHandMethods(unittest.TestCase):
    """Tests the hand class"""

    def test_check_num(self):
        """Checks that we can find sets of the same number in a deck"""
        deck = Deck()
        deck.empty_deck()
        deck.add_cards(["2Clubs", "2Spades", "2Diamonds"])
        self.assertEqual(len(Hand.get_num_sets(deck)), 1)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.get_num_sets(deck)[0])
        deck.add_card("2Hearts")
        self.assertEqual(len(Hand.get_num_sets(deck)), 1)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.get_num_sets(deck)[0])
        deck.remove_card("2Clubs")
        self.assertEqual(len(Hand.get_num_sets(deck)), 1)
        for card in ["2Hearts", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.get_num_sets(deck)[0])
        deck.remove_card("2Spades")
        self.assertEqual(len(Hand.get_num_sets(deck)), 0)
        deck.add_card("3Spades")
        self.assertEqual(len(Hand.get_num_sets(deck)), 0)
        deck.add_cards(["QHearts","QSpades", "QDiamonds", "2Clubs", "2Spades"])
        self.assertEqual(len(Hand.get_num_sets(deck)), 2)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.get_num_sets(deck)[0])
        for card in ["QHearts", "QSpades", "QDiamonds"]:
            self.assertTrue(card in Hand.get_num_sets(deck)[1])

    def test_check_run(self):
        """Checks that we can find runs in a deck"""
        deck = Deck()
        deck.empty_deck()
        deck.add_cards(["2Clubs", "2Spades"])
        self.assertEqual(len(Hand.get_run_sets(deck)), 0)
        deck.add_cards(["3Spades", "4Clubs", "3Clubs"])
        self.assertEqual(len(Hand.get_run_sets(deck)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in Hand.get_run_sets(deck)[0])
        deck.remove_card("3Spades")
        deck.add_card("5Clubs")
        self.assertEqual(len(Hand.get_run_sets(deck)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs", "5Clubs"]:
            self.assertTrue(card in Hand.get_run_sets(deck)[0])
        deck.remove_card("5Clubs")
        deck.add_card("AClubs")
        self.assertEqual(len(Hand.get_run_sets(deck)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in Hand.get_run_sets(deck)[0])
        deck.add_cards(["JClubs", "QClubs", "KClubs"])
        self.assertEqual(len(Hand.get_run_sets(deck)), 2)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in Hand.get_run_sets(deck)[0])

        for card in ["AClubs", "JClubs", "QClubs", "KClubs"]:
            self.assertTrue(card in Hand.get_run_sets(deck)[1])
        deck.empty_deck()
        deck.add_cards(["QClubs", "KClubs", "AClubs"])
        self.assertEqual(len(Hand.get_run_sets(deck)), 1)
        for card in ["AClubs", "QClubs", "KClubs"]:
            self.assertTrue(card in Hand.get_run_sets(deck)[0])

    def test_set_scores(self):
        """Checks that we calculate the score of a hand correctly"""
        deck = Deck()
        deck.empty_deck()
        deck.add_cards(["2Clubs", "2Spades"])
        self.assertEqual(Hand.get_set_score(Hand.get_run_sets(deck)), 0)
        deck.add_cards(["3Spades", "4Clubs", "3Clubs"])
        self.assertEqual(Hand.get_set_score(Hand.get_run_sets(deck)[0]), 9)
        deck.remove_card("3Spades")
        deck.add_card("5Clubs")
        self.assertEqual(Hand.get_set_score(Hand.get_run_sets(deck)[0]), 14)
        deck.remove_card("5Clubs")
        # ace is high
        deck.add_card("AClubs")
        self.assertEqual(Hand.get_set_score(Hand.get_run_sets(deck)[0]), 9)
        deck.add_cards(["JClubs", "QClubs", "KClubs"])
        self.assertEqual(Hand.get_set_score(Hand.get_run_sets(deck)[0]), 9)
        self.assertEqual(Hand.get_set_score(Hand.get_run_sets(deck)[1]), 45)
        deck.empty_deck()
        deck.add_cards(["QClubs", "KClubs", "AClubs"])
        self.assertEqual(Hand.get_set_score(Hand.get_run_sets(deck)[0]), 35)

    def test_get_sets(self):
        """Checks that we find all the sets in a deck"""
        hand = Hand()
        num_sets, run_sets = hand.get_sets()
        res_arr = [['2Hearts', '2Diamonds', '2Spades', '2Clubs'], \
        ['3Hearts', '3Diamonds', '3Spades', '3Clubs'], \
        ['4Hearts', '4Diamonds', '4Spades', '4Clubs'], \
        ['5Hearts', '5Diamonds', '5Spades', '5Clubs'], \
        ['6Hearts', '6Diamonds', '6Spades', '6Clubs'], \
        ['7Hearts', '7Diamonds', '7Spades', '7Clubs'], \
        ['8Hearts', '8Diamonds', '8Spades', '8Clubs'], \
        ['9Hearts', '9Diamonds', '9Spades', '9Clubs'], \
        ['THearts', 'TDiamonds', 'TSpades', 'TClubs'], \
        ['JHearts', 'JDiamonds', 'JSpades', 'JClubs'], \
        ['QHearts', 'QDiamonds', 'QSpades', 'QClubs'], \
        ['KHearts', 'KDiamonds', 'KSpades', 'KClubs'], \
        ['AHearts', 'ADiamonds', 'ASpades', 'AClubs']]
        self.assertEqual(sorted(num_sets), sorted(res_arr))
        self.assertEqual([], run_sets)
        hand.empty_deck()
        hand.add_cards(["2Hearts", "3Hearts", "4Hearts", "6Hearts", "6Clubs", "6Spades"])
        num_sets, run_sets = hand.get_sets()
        res_arr = [["6Hearts", "6Spades", "6Clubs"]]
        res_arr2 = [["2Hearts", "3Hearts", "4Hearts"]]
        self.assertEqual(sorted(num_sets), sorted(res_arr))
        self.assertEqual(sorted(run_sets), sorted(res_arr2))
        # Example of a bad case:
        hand.empty_deck()
        hand.add_cards(["2Hearts", "3Hearts", "4Hearts", "5Hearts", "6Hearts", "6Clubs", "6Spades"])
        num_sets, run_sets = hand.get_sets()
        res_arr = [["6Hearts", "6Spades", "6Clubs"]]
        res_arr2 = []
        self.assertEqual(sorted(num_sets), sorted(res_arr))
        self.assertEqual(sorted(run_sets), sorted(res_arr2))

    def test_get_sets_and_scores(self):
        """Checks that we can find all the sets and get their scores"""
        hand = Hand()
        scores, sets = hand.get_set_scores()
        res_arr = [['2Hearts', '2Diamonds', '2Spades', '2Clubs'], \
        ['3Hearts', '3Diamonds', '3Spades', '3Clubs'], \
        ['4Hearts', '4Diamonds', '4Spades', '4Clubs'], \
        ['5Hearts', '5Diamonds', '5Spades', '5Clubs'], \
        ['6Hearts', '6Diamonds', '6Spades', '6Clubs'], \
        ['7Hearts', '7Diamonds', '7Spades', '7Clubs'], \
        ['8Hearts', '8Diamonds', '8Spades', '8Clubs'], \
        ['9Hearts', '9Diamonds', '9Spades', '9Clubs'], \
        ['THearts', 'TDiamonds', 'TSpades', 'TClubs'], \
        ['JHearts', 'JDiamonds', 'JSpades', 'JClubs'], \
        ['QHearts', 'QDiamonds', 'QSpades', 'QClubs'], \
        ['KHearts', 'KDiamonds', 'KSpades', 'KClubs'], \
        ['AHearts', 'ADiamonds', 'ASpades', 'AClubs']]
        self.assertEqual(sorted(sets), sorted(res_arr))
        self.assertEqual(scores, [8, 12, 16, 20, 24, 28, 32, 36, 40, 40, 40, 40, 60])


if __name__ == '__main__':
    unittest.main()
