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
        self.assertEqual(len(checkNum(d)), 1)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in checkNum(d)[0])
        d.addCard("2Hearts")
        self.assertEqual(len(checkNum(d)), 1)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in checkNum(d)[0])
        d.removeCard("2Clubs")
        self.assertEqual(len(checkNum(d)), 1)
        for card in ["2Hearts", "2Spades", "2Diamonds"]:
            self.assertTrue(card in checkNum(d)[0])
        d.removeCard("2Spades")
        self.assertEqual(len(checkNum(d)), 0)
        d.addCard("3Spades")
        self.assertEqual(len(checkNum(d)), 0)
        d.addCards(["QHearts","QSpades", "QDiamonds", "2Clubs", "2Spades"])
        self.assertEqual(len(checkNum(d)), 2)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in checkNum(d)[0])
        for card in ["QHearts", "QSpades", "QDiamonds"]:
            self.assertTrue(card in checkNum(d)[1])

    def testCheckRun(self):
        d = Deck()
        d.emptyDeck()
        d.addCards(["2Clubs", "2Spades"])
        self.assertEqual(len(checkRun(d)), 0)
        d.addCards(["3Spades", "4Clubs", "3Clubs"])
        self.assertEqual(len(checkRun(d)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in checkRun(d)[0])
        d.removeCard("3Spades")
        d.addCard("5Clubs")
        self.assertEqual(len(checkRun(d)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs", "5Clubs"]:
            self.assertTrue(card in checkRun(d)[0])
        d.removeCard("5Clubs")
        d.addCard("AClubs")
        self.assertEqual(len(checkRun(d)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in checkRun(d)[0])
        d.addCards(["JClubs", "QClubs", "KClubs"])
        self.assertEqual(len(checkRun(d)), 2)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in checkRun(d)[0])

        for card in ["AClubs", "JClubs", "QClubs", "KClubs"]:
            self.assertTrue(card in checkRun(d)[1])
        d.emptyDeck()
        d.addCards(["QClubs", "KClubs", "AClubs"])
        self.assertEqual(len(checkRun(d)), 1)
        for card in ["AClubs", "QClubs", "KClubs"]:
            self.assertTrue(card in checkRun(d)[0])

if __name__ == '__main__':
    unittest.main()
