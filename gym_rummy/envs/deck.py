# A simple deck class
# A deck is a dictionary mapping
# of the form number and suite
# it contains a 1 if the value is contained 
# and either has a 0 or does not contain
# the key otherwise
# Example:
# Deck contains JHeart
# would be the jack of hearts
# Mapping Key:
# A = ace
# K = king
# Q = queen
# J = jack
# T = ten
# 9 = nine
# 8 = eight
# 7 = seven
# 6 = six
# 5 = five
# 4 = four
# 3 = three
# 2 = two
# Suites include Hearts, Spades, Clubs, and Diamonds

import numpy as np
import random

class Deck:
    def __init__(self, deck = None):
        if deck is None:
            self.deck = self.buildFullDeck()
        else:
            self.deck = deck

    def __contains__(self, card):
        return card in self.deck and self.deck[card] == 1

    def __repr__(self):
        ret = ""
        for card in self.deck:
            if(self.deck[card] == 1):
                ret += card + "\n"
        return ret

    def buildFullDeck(self):
        deck = {}
        buildMapSuite = {0: "Hearts", 1: "Spades", 2:"Clubs", 3: "Diamonds"}
        buildMapNum = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}
        for i in range(4):
            for j in range(2, 15):
                if j > 9:
                    deck[buildMapNum[j]+buildMapSuite[i]] = 1
                else:
                    deck[str(j) + buildMapSuite[i]] = 1
        return deck

    def addCard(self, card):
        if card in self.deck:
            raise ValueError("Card " + card + " already in deck!")
        else:
            self.deck[card] = 1

    def removeCard(self, card):
        if card not in self.deck: 
            raise ValueError("Card " + card + " not in deck!")
        else:
            self.deck.pop(card)

    def addCards(self, cards):
        for card in cards:
            self.addCard(card)

    def removeCards(self, cards):
        for card in cards:
            self.removeCard(card)

    def __len__(self):
        return len(self.deck)

    def emptyDeck(self):
        self.deck = {}
    
    # Removes all cards of same number. Returns the number of cards removed
    def removeCardNum(self, num):
        buildMapSuite = {0: "Hearts", 1: "Spades", 2:"Clubs", 3: "Diamonds"}
        count = 0
        for i in range(4):
            if num + buildMapSuite[i] in self.deck:
                self.removeCard(num+buildMapSuite[i])
                count += 1
        return count

    # Removes all cards of same suite. Returns the number of cards removed
    def removeCardSuite(self, suite):
        buildMapNum = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}
        count = 0
        for i in range(2, 15):
            if i > 9 and buildMapNum[i] + suite in self.deck:
                self.removeCard(buildMapNum[i]+suite)
                count += 1
            elif str(i) + suite in self.deck:
                self.removeCard(str(i)+suite)
                count += 1
        return count
    
    # Matrix form for checking runs and suits. Rows go as hearts, dia, spade, club. 
    # Columns go ace to king with ace as 1. Binary 1 if card is present, 0 ow.
    def toNumpy(self):
        numMap = {'A': 12, '2':0, '3':1, '4':2, '5':3, '6': 4, '7':5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11}
        suiteMap = {'Hearts': 0, 'Diamonds': 1, 'Spades':2, 'Clubs':3}
        mat = np.zeros((4, 13))
        for card in self.deck:
            mat[suiteMap[card[1:]]][numMap[card[0]]] = 1
        return mat

    @classmethod
    def fromNumpy(cls, mat):
        deck = {}
        numMap = {12: 'A', 0:'2', 1:'3', 2:'4', 3:'5', 4: '6', 5:'7', 6:'8', 7: '9', 8: 'T', 9: 'J', 10: 'Q', 11: 'K'}
        suiteMap = {0:'Hearts', 1:'Diamonds', 2:'Spades', 3:'Clubs'}
        assert(mat.shape[0] == 4 and mat.shape[1] == 13)
        for i in range(4):
            for j in range(13):
                if mat[i][j] == 1:
                    deck[numMap[j] + suiteMap[i]] = 1
        return Deck(deck)

    # Iterator. We cannot modify while iterating
    def __iter__(self):
        self.it = iter(self.deck)
        return self

    def __next__(self):
        return next(self.it)

    def __eq__(self, rhs):
        return self.deck == rhs.deck

    def drawRandom(self):
        choice = random.choice(list(self.deck))
        self.removeCard(choice)
        return choice
