import unittest

import sys
sys.path.append("./src")
from deck import Deck
from util import checkNum, checkRun

class TestUtilMethods(unittest.TestCase):
    def testCheckNum(self):
        d = Deck()
        d.emptyDeck()
        d.addCards(["2Clubs", "2Spades", "2Diamonds"])
        self.assertTrue(checkNum(d))
        d.addCard("2Hearts")
        self.assertTrue(checkNum(d))
        d.removeCard("2Clubs")
        self.assertTrue(checkNum(d))
        d.removeCard("2Spades")
        self.assertFalse(checkNum(d))
        d.addCard("3Spades")
        self.assertFalse(checkNum(d))
        d.emptyDeck()
        d.addCards(["QHearts","QSpades", "QDiamonds"])
        self.assertTrue(checkNum(d))

    def testCheckRun(self):
        d = Deck()
        d.emptyDeck()
        d.addCards(["2Clubs", "2Spades"])
        self.assertFalse(checkRun(d))
        d.emptyDeck()
        d.addCards(["2Clubs", "3Spades", "4Clubs"])
        self.assertFalse(checkRun(d))
        d.removeCard("3Spades")
        d.addCard("5Clubs")
        self.assertFalse(checkRun(d))
        d.removeCard("5Clubs")
        d.addCard("3Clubs")
        self.assertTrue(checkRun(d))
        d.emptyDeck()
        d.addCards(["JClubs", "QClubs", "KClubs"])
        self.assertTrue(checkRun(d))
        d.emptyDeck()
        d.addCards(["JClubs", "QClubs", "KClubs", "AClubs"])
        self.assertTrue(checkRun(d))
        d.emptyDeck()
        d.addCards(["2Clubs", "3Clubs", "4Clubs", "AClubs"])
        self.assertTrue(checkRun(d))
        d.emptyDeck()
        d.addCards(["5Clubs", "3Clubs", "4Clubs", "AClubs"])
        self.assertFalse(checkRun(d))
        d2 = Deck()
        self.assertFalse(checkRun(d2))
 
if __name__ == '__main__':
    unittest.main()
