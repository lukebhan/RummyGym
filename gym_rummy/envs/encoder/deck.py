"""A simple deck class"""
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

import random
import numpy as np

class Deck:
    """A class for a deck of cards"""

    def __init__(self, deck = None):
        """Creates a deck of cards"""
        if deck is None:
            self.deck = self.build_full_deck()
        else:
            self.deck = deck
        self.iter = None

    def __contains__(self, card):
        """Sees if a specific card is contained in the deck"""
        return card in self.deck and self.deck[card] == 1

    def __repr__(self):
        """Gives a string representation of the deck"""
        ret = ""
        for card in self.deck:
            if self.deck[card] == 1:
                ret += card + "\n"
        return ret

    @classmethod
    def build_full_deck(cls):
        """Creates a standard deck of 52 cards"""
        deck = {}
        build_map_suite = {0: "Hearts", 1: "Spades", 2:"Clubs", 3: "Diamonds"}
        build_map_num = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}
        for i in range(4):
            for j in range(2, 15):
                if j > 9:
                    deck[build_map_num[j]+build_map_suite[i]] = 1
                else:
                    deck[str(j) + build_map_suite[i]] = 1
        return deck

    def add_card(self, card):
        """Adds one specific card to deck"""
        if card in self.deck:
            raise ValueError("Card " + card + " already in deck!")
        self.deck[card] = 1

    def remove_card(self, card):
        """Removes one specific card to deck"""
        if card not in self.deck:
            raise ValueError("Card " + card + " not in deck!")
        self.deck.pop(card)

    def add_cards(self, cards):
        """Adds multiple cards to the deck"""
        for card in cards:
            self.add_card(card)

    def remove_cards(self, cards):
        """Removes multiple cards from the deck"""
        for card in cards:
            self.remove_card(card)

    def __len__(self):
        """Returns the number of cards in the deck"""
        return len(self.deck)

    def empty_deck(self):
        """Empties the deck"""
        self.deck = {}

    def remove_card_num(self, num):
        """Removes all cards of the same number; returns the number of cards removed"""
        build_map_suite = {0: "Hearts", 1: "Spades", 2:"Clubs", 3: "Diamonds"}
        count = 0
        for i in range(4):
            if num + build_map_suite[i] in self.deck:
                self.remove_card(num+build_map_suite[i])
                count += 1
        return count

    def remove_card_suite(self, suite):
        """Removes all cards of same suite. Returns the number of cards removed"""
        build_map_num = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}
        count = 0
        for i in range(2, 15):
            if i > 9 and build_map_num[i] + suite in self.deck:
                self.remove_card(build_map_num[i]+suite)
                count += 1
            elif str(i) + suite in self.deck:
                self.remove_card(str(i)+suite)
                count += 1
        return count

    def to_numpy(self):
        """Matrix form of deck of cards for checking runs and suits. \
        The rows go as hearts, diamonds, spades, and clubs. \
        Columns go ace to king with ace as 1. Binary 1 if king is present, 0 o.w."""
        num_map = {'A': 12, '2':0, '3':1, '4':2, '5':3, '6': 4, \
        '7':5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11}
        suite_map = {'Hearts': 0, 'Diamonds': 1, 'Spades':2, 'Clubs':3}
        mat = np.zeros((4, 13))
        for card in self.deck:
            mat[suite_map[card[1:]]][num_map[card[0]]] = 1
        return mat

    @classmethod
    def from_numpy(cls, mat):
        """Maps deck to numpy arrays"""
        deck = {}
        num_map = {12: 'A', 0:'2', 1:'3', 2:'4', 3:'5', 4: '6', \
        5:'7', 6:'8', 7: '9', 8: 'T', 9: 'J', 10: 'Q', 11: 'K'}
        suite_map = {0:'Hearts', 1:'Diamonds', 2:'Spades', 3:'Clubs'}
        assert(mat.shape[0] == 4 and mat.shape[1] == 13)
        for i in range(4):
            for j in range(13):
                if mat[i][j] == 1:
                    deck[num_map[j] + suite_map[i]] = 1
        return Deck(deck)

    def __iter__(self):
        """Iterator method, unmodifiable while iterating"""
        self.iter = iter(self.deck)
        return self

    def __next__(self):
        """Gets next iterator"""
        return next(self.iter)

    def __eq__(self, rhs):
        """Checks if a deck is equal to another deck"""
        return self.deck == rhs.deck

    def draw_random(self):
        """Gets a random card from the deck"""
        choice = random.choice(list(self.deck))
        self.remove_card(choice)
        return choice
