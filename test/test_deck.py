import unittest

import sys
sys.path.append("./src")
from deck import Deck

class TestDeckMethods(unittest.TestCase):
    def testDefaultConstructor(self):
        d = Deck()
        self.assertEqual(len(d), 52)

    def testEmptyDeck(self):
        d = Deck()
        self.assertEqual(len(d), 52)
        d.emptyDeck()
        self.assertEqual(len(d), 0)

    def testAlternateConstructor(self):
        d = Deck()
        d.emptyDeck()
        d2 = Deck(d)
        self.assertEqual(len(d2), 0)

    def testContains(self):
        d = Deck()
        card = "JHearts"
        self.assertTrue(card in d)
        card = "8Clubs"
        self.assertTrue(card in d)

    def testAddCard(self):
        d = Deck()
        d.emptyDeck()
        d.addCard("ASpades")
        self.assertEqual(len(d), 1)
        self.assertEqual("ASpades\n", str(d))
        self.assertFalse("JClubs" in d)

    def testAddCards(self):
        d = Deck()
        d.emptyDeck()
        self.assertEqual("", str(d))
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        d.addCards(cards)
        self.assertEqual(len(d), 8)
        self.assertTrue("2Clubs"in d)

    def testRemoveCard(self):
        d = Deck()
        d.emptyDeck()
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        d.addCards(cards)
        self.assertEqual(len(d), 8)
        d.removeCard("ASpades")
        self.assertEqual(len(d), 7)
        self.assertFalse("ASpades" in d)

    def testRemoveCards(self):
        d = Deck()
        d.emptyDeck()
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        d.addCards(cards)
        self.assertEqual(len(d), 8)
        d.removeCards(cards[0:4])
        self.assertEqual(len(d), 4)

    def testRepr(self):
        d = Deck()
        d.emptyDeck()
        cards = ["ASpades" , "AClubs", "ADiamonds", "AHearts", "2Spades", "2Clubs", "2Diamonds", "2Hearts"]
        d.addCards(cards)
        self.assertEqual(len(d), 8)
        ret = "" 
        for val in cards:
            ret = val + "\n"
        self.assertTrue(ret in  str(d))

    def testRemoveCardNum(self):
        d = Deck()
        self.assertEqual(4, d.removeCardNum("2"))
        self.assertEqual(len(d), 48)
        self.assertEqual(4, d.removeCardNum("Q"))
        self.assertEqual(len(d), 44)
        d.addCard("QSpades")
        self.assertEqual(1, d.removeCardNum("Q"))

    def testRemoveCardSuite(self):
        d = Deck()
        self.assertEqual(13, d.removeCardSuite("Spades"))
        self.assertEqual(len(d), 39)
        self.assertEqual(3, d.removeCardNum("Q"))
        self.assertEqual(len(d), 36)
        d.addCard("ASpades")
        self.assertEqual(0, d.removeCardNum("Q"))
        self.assertEqual(1, d.removeCardSuite("Spades"))

    def testIterator(self):
        d = Deck()
        ret = "" 
        count = 0
        for card in d:
            ret += card + "\n"
            count += 1
        self.assertTrue(ret in str(d))
        self.assertEqual(52, count)
 
if __name__ == '__main__':
    unittest.main()
