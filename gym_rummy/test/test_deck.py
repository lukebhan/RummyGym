""" A unittesting framework for the Deck Class """
import sys
import unittest
import numpy as np
sys.path.append("./envs")
from deck import Deck #pylint: disable=E0401,C0413

class TestDeckMethods(unittest.TestCase):
    """ Tests the Deck Class """
    def test_default_constructor(self):
        """ Tests we can build a deck """
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_empty_deck(self):
        """ Tests we can build an empty deck """
        deck = Deck()
        self.assertEqual(len(deck), 52)
        deck.emptyDeck()
        self.assertEqual(len(deck), 0)

    def test_alternate_constructor(self):
        """ Tests we can build a deck from another """
        deck = Deck()
        deck.emptyDeck()
        d_two = Deck(deck)
        self.assertEqual(len(d_two), 0)

    def test_contains(self):
        """ Tests our contains special method """
        deck = Deck()
        card = "JHearts"
        self.assertTrue(card in deck)
        card = "8Clubs"
        self.assertTrue(card in deck)

    def test_add_card(self):
        """ Tests we can add a card """
        deck = Deck()
        deck.emptyDeck()
        deck.addCard("ASpades")
        self.assertEqual(len(deck), 1)
        self.assertEqual("ASpades\n", str(deck))
        self.assertFalse("JClubs" in deck)

    def test_add_cards(self):
        """ Tests we can add cards from a list """
        deck = Deck()
        deck.emptyDeck()
        self.assertEqual("", str(deck))
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", \
                "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        deck.addCards(cards)
        self.assertEqual(len(deck), 8)
        self.assertTrue("2Clubs"in deck)

    def test_remove_card(self):
        """ Tests removing a card from deck """
        deck = Deck()
        deck.emptyDeck()
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", \
                "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        deck.addCards(cards)
        self.assertEqual(len(deck), 8)
        deck.removeCard("ASpades")
        self.assertEqual(len(deck), 7)
        self.assertFalse("ASpades" in deck)

    def test_remove_cards(self):
        """ Tests we can remove list of cards """
        deck = Deck()
        deck.emptyDeck()
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", \
                "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        deck.addCards(cards)
        self.assertEqual(len(deck), 8)
        deck.removeCards(cards[0:4])
        self.assertEqual(len(deck), 4)

    def test_repr(self):
        """ Tests we can print properly """
        deck = Deck()
        deck.emptyDeck()
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", \
                "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        deck.addCards(cards)
        self.assertEqual(len(deck), 8)
        ret = ""
        for val in cards:
            ret = val + "\n"
        self.assertTrue(ret in  str(deck))

    def test_remove_card_num(self):
        """ Tests a card can be removed """
        deck = Deck()
        self.assertEqual(4, deck.removeCardNum("2"))
        self.assertEqual(len(deck), 48)
        self.assertEqual(4, deck.removeCardNum("Q"))
        self.assertEqual(len(deck), 44)
        deck.addCard("QSpades")
        self.assertEqual(1, deck.removeCardNum("Q"))

    def test_remove_card_suite(self):
        """ Tests a card can be removed by suite """
        deck = Deck()
        self.assertEqual(13, deck.removeCardSuite("Spades"))
        self.assertEqual(len(deck), 39)
        self.assertEqual(3, deck.removeCardNum("Q"))
        self.assertEqual(len(deck), 36)
        deck.addCard("ASpades")
        self.assertEqual(0, deck.removeCardNum("Q"))
        self.assertEqual(1, deck.removeCardSuite("Spades"))

    def test_iterator(self):
        """ Tests an iterator is working over dec. Maintains order """
        deck = Deck()
        ret = ""
        count = 0
        for card in deck:
            ret += card + "\n"
            count += 1
        self.assertTrue(ret in str(deck))
        self.assertEqual(52, count)

    def test_to_numpy(self):
        """ Tests we can convert deck to numpy Matrix """
        deck = Deck()
        self.assertEqual(deck.toNumpy().all(), np.full((4, 13), 1).all())
        deck.emptyDeck()
        self.assertEqual(deck.toNumpy().all(), np.zeros((4, 13)).all())
        deck.addCards(["ASpades", "JClubs", "8Hearts", "4Diamonds"])
        mat = np.zeros((4, 13))
        mat[1][2] = 1
        mat[0][6] = 1
        mat[2][12] = 1
        mat[3][9] = 1
        self.assertEqual(deck.toNumpy().all(),mat.all())

    def test_from_numpy(self):
        """ Tests we can build deck from numpy """
        mat = np.zeros((4, 13))
        deck = Deck()
        deck.emptyDeck()
        d_two = Deck.fromNumpy(mat)
        self.assertEqual(deck, d_two)
        deck.addCards(["ASpades", "JClubs", "8Hearts", "4Diamonds"])
        mat[0][6]= 1
        mat[1][2] = 1
        mat[2][12] = 1
        mat[3][9] = 1
        self.assertEqual(deck, Deck.fromNumpy(mat))

    def test_equals(self):
        """ Tests two decks are equal """
        d_one = Deck()
        d_two = Deck()
        self.assertEqual(d_one, d_two)
        d_one.emptyDeck()
        d_two.emptyDeck()
        self.assertEqual(d_one, d_two)
        d_one.addCards(["ASpades", "2Clubs"])
        d_two.addCards(["ASpades", "2Clubs"])
        self.assertEqual(d_one, d_two)
        d_two.removeCard("ASpades")
        self.assertFalse(d_one == d_two)

    def test_random_draw(self):
        """ Tests random drawing in player class """
        d_one = Deck()
        self.assertEqual(len(d_one), 52)
        d_one.drawRandom()
        self.assertEqual(len(d_one), 51)
        for i in range(50):
            d_one.drawRandom()
            self.assertEqual(len(d_one), 50-i)
        d_one.drawRandom()
        self.assertEqual(len(d_one), 0)
        self.assertRaises(IndexError, d_one.drawRandom)

if __name__ == '__main__':
    unittest.main()
