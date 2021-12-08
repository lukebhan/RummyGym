"""A player class. Contains the players hand as a state, along with their possible actions."""

import sys
sys.path.append("./envs")
from hand import Hand #pylint: disable=E0401,C0413

class Player():
    """Creates a player"""

    def __init__(self, starterDeck, name=None, verbose=False):
        """Creates one player"""
        self.name = name
        self.hand = Hand(starterDeck)
        self.score = 0
        self.verbose = verbose

    def place_sets(self):
        """Places sets down on table"""
        scores, sets = self.hand.get_set_scores()
        for score, set_val in zip(scores, sets):
            self.score += score
            for card in set_val:
                self.hand.remove_card(card)

    def get_score(self):
        """Gets current score"""
        return self.score

    def discard(self, index, discard_deck):
        """Discards a card to discard deck"""
        if index >= len(self.hand):
            raise IndexError("Trying to discard a index that is not feasible")
        iterable = iter(self.hand)
        card = next(iterable)
        for _ in range(1, index+1):
            card=next(iterable)
        if self.verbose:
            print(self.name + " Discards " + card)
        discard_deck.add_card(card)
        self.hand.remove_card(card)

    def pickup_pile(self, discard_deck):
        """Picks up from discard pile"""
        length = len(discard_deck)
        if length == 1:
            # only one random card to draw
            card = discard_deck.draw_random()
            self.hand.add_card(card)
            return
        iterable = iter(discard_deck)
        to_discard = []
        for _ in range(length//2):
            card = next(iterable)
            self.hand.add_card(card)
            to_discard.append(card)
        for card in to_discard:
            discard_deck.remove_card(card)

    def draw_card(self, draw_deck):
        """Draws a card from deck"""
        card = draw_deck.draw_random()
        self.hand.add_card(card)

    def get_hand(self):
        """Gets hand of player"""
        return self.hand

    def take_turn(self, action, draw_deck, discard_deck):
        """Player takes one turn: draws card or picks up from deck,\
        places sets down, discards a card"""
        if self.verbose:
            print(self.name + " Turn. Score is ", str(self.score))
        draw_decision = action[0]
        if len(draw_deck) != 0 or len(discard_deck) != 0:
            if draw_decision > 0.5 or len(draw_deck) == 0:
                if self.verbose:
                    print(self.name + " Picks up half the discard deck! (" \
                    + str(len(discard_deck)) + " cards)")
                self.pickup_pile(discard_deck)
            else:
                self.draw_card(draw_deck)
                if self.verbose:
                    print(self.name + " Picks up a card from the draw pile!")

        self.place_sets()
        discard_decision = round(action[1]*(len(self.hand)-1))
        if len(self.hand) != 0:
            self.discard(discard_decision, discard_deck)
        if self.verbose:
            print(self.name + "'s hand looks like:")
            print(self.hand)
        return len(self.hand)
