import unittest

import sys
sys.path.append("./envs")
from deck import Deck
from hand import Hand

class TestHandMethods(unittest.TestCase):
    def testCheckNum(self):
        d = Deck()
        d.emptyDeck()
        d.addCards(["2Clubs", "2Spades", "2Diamonds"])
        self.assertEqual(len(Hand.getNumSets(d)), 1)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.getNumSets(d)[0])
        d.addCard("2Hearts")
        self.assertEqual(len(Hand.getNumSets(d)), 1)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.getNumSets(d)[0])
        d.removeCard("2Clubs")
        self.assertEqual(len(Hand.getNumSets(d)), 1)
        for card in ["2Hearts", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.getNumSets(d)[0])
        d.removeCard("2Spades")
        self.assertEqual(len(Hand.getNumSets(d)), 0)
        d.addCard("3Spades")
        self.assertEqual(len(Hand.getNumSets(d)), 0)
        d.addCards(["QHearts","QSpades", "QDiamonds", "2Clubs", "2Spades"])
        self.assertEqual(len(Hand.getNumSets(d)), 2)
        for card in ["2Clubs", "2Spades", "2Diamonds"]:
            self.assertTrue(card in Hand.getNumSets(d)[0])
        for card in ["QHearts", "QSpades", "QDiamonds"]:
            self.assertTrue(card in Hand.getNumSets(d)[1])

    def testCheckRun(self):
        d = Deck()
        d.emptyDeck()
        d.addCards(["2Clubs", "2Spades"])
        self.assertEqual(len(Hand.getRunSets(d)), 0)
        d.addCards(["3Spades", "4Clubs", "3Clubs"])
        self.assertEqual(len(Hand.getRunSets(d)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in Hand.getRunSets(d)[0])
        d.removeCard("3Spades")
        d.addCard("5Clubs")
        self.assertEqual(len(Hand.getRunSets(d)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs", "5Clubs"]:
            self.assertTrue(card in Hand.getRunSets(d)[0])
        d.removeCard("5Clubs")
        d.addCard("AClubs")
        self.assertEqual(len(Hand.getRunSets(d)), 1)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in Hand.getRunSets(d)[0])
        d.addCards(["JClubs", "QClubs", "KClubs"])
        self.assertEqual(len(Hand.getRunSets(d)), 2)
        for card in ["2Clubs",  "3Clubs", "4Clubs"]:
            self.assertTrue(card in Hand.getRunSets(d)[0])

        for card in ["AClubs", "JClubs", "QClubs", "KClubs"]:
            self.assertTrue(card in Hand.getRunSets(d)[1])
        d.emptyDeck()
        d.addCards(["QClubs", "KClubs", "AClubs"])
        self.assertEqual(len(Hand.getRunSets(d)), 1)
        for card in ["AClubs", "QClubs", "KClubs"]:
            self.assertTrue(card in Hand.getRunSets(d)[0])

    def testSetScores(self):
        d = Deck()
        d.emptyDeck()
        d.addCards(["2Clubs", "2Spades"])
        self.assertEqual(Hand.getSetScore(Hand.getRunSets(d)), 0)
        d.addCards(["3Spades", "4Clubs", "3Clubs"])
        self.assertEqual(Hand.getSetScore(Hand.getRunSets(d)[0]), 9)
        d.removeCard("3Spades")
        d.addCard("5Clubs")
        self.assertEqual(Hand.getSetScore(Hand.getRunSets(d)[0]), 14)
        d.removeCard("5Clubs")
        # ace is high
        d.addCard("AClubs")
        self.assertEqual(Hand.getSetScore(Hand.getRunSets(d)[0]), 9)
        d.addCards(["JClubs", "QClubs", "KClubs"])
        self.assertEqual(Hand.getSetScore(Hand.getRunSets(d)[0]), 9)
        self.assertEqual(Hand.getSetScore(Hand.getRunSets(d)[1]), 45)
        d.emptyDeck()
        d.addCards(["QClubs", "KClubs", "AClubs"])
        self.assertEqual(Hand.getSetScore(Hand.getRunSets(d)[0]), 35)

    def testGetSets(self):
        h = Hand()
        numSets, runSets = h.getSets()
        resArr = [['2Hearts', '2Diamonds', '2Spades', '2Clubs'], ['3Hearts', '3Diamonds', '3Spades', '3Clubs'], ['4Hearts', '4Diamonds', '4Spades', '4Clubs'], ['5Hearts', '5Diamonds', '5Spades', '5Clubs'], ['6Hearts', '6Diamonds', '6Spades', '6Clubs'], ['7Hearts', '7Diamonds', '7Spades', '7Clubs'], ['8Hearts', '8Diamonds', '8Spades', '8Clubs'], ['9Hearts', '9Diamonds', '9Spades', '9Clubs'], ['THearts', 'TDiamonds', 'TSpades', 'TClubs'], ['JHearts', 'JDiamonds', 'JSpades', 'JClubs'], ['QHearts', 'QDiamonds', 'QSpades', 'QClubs'], ['KHearts', 'KDiamonds', 'KSpades', 'KClubs'], ['AHearts', 'ADiamonds', 'ASpades', 'AClubs']]
        self.assertEqual(sorted(numSets), sorted(resArr))
        self.assertEqual([], runSets)
        h = Hand()
        h.emptyDeck()
        h.addCards(["2Hearts", "3Hearts", "4Hearts", "6Hearts", "6Clubs", "6Spades"])
        numSets, runSets = h.getSets()
        resArr = [["6Hearts", "6Spades", "6Clubs"]]
        resArr2 = [["2Hearts", "3Hearts", "4Hearts"]]
        self.assertEqual(sorted(numSets), sorted(resArr))
        self.assertEqual(sorted(runSets), sorted(resArr2))
        # Example of a bad case:
        h.emptyDeck()
        h.addCards(["2Hearts", "3Hearts", "4Hearts", "5Hearts", "6Hearts", "6Clubs", "6Spades"])
        numSets, runSets = h.getSets()
        resArr = [["6Hearts", "6Spades", "6Clubs"]]
        resArr2 = []
        self.assertEqual(sorted(numSets), sorted(resArr))
        self.assertEqual(sorted(runSets), sorted(resArr2))

    def testGetSetsAndScores(self):
        h = Hand()
        scores, sets = h.getSetScores()
        resArr = [['2Hearts', '2Diamonds', '2Spades', '2Clubs'], ['3Hearts', '3Diamonds', '3Spades', '3Clubs'], ['4Hearts', '4Diamonds', '4Spades', '4Clubs'], ['5Hearts', '5Diamonds', '5Spades', '5Clubs'], ['6Hearts', '6Diamonds', '6Spades', '6Clubs'], ['7Hearts', '7Diamonds', '7Spades', '7Clubs'], ['8Hearts', '8Diamonds', '8Spades', '8Clubs'], ['9Hearts', '9Diamonds', '9Spades', '9Clubs'], ['THearts', 'TDiamonds', 'TSpades', 'TClubs'], ['JHearts', 'JDiamonds', 'JSpades', 'JClubs'], ['QHearts', 'QDiamonds', 'QSpades', 'QClubs'], ['KHearts', 'KDiamonds', 'KSpades', 'KClubs'], ['AHearts', 'ADiamonds', 'ASpades', 'AClubs']]
        self.assertEqual(sorted(sets), sorted(resArr))
        self.assertEqual(scores, [8, 12, 16, 20, 24, 28, 32, 36, 40, 40, 40, 40, 60])


if __name__ == '__main__':
    unittest.main()
