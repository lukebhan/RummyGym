"""A player class. Contains the players hand as a state, along with their possible actions."""

import sys
sys.path.append("./envs")
from hand import Hand #pylint: disable=E0401,C0413

class Player():
    """Creates a player"""

    def __init__(self, starter_deck):
        """Creates one player"""
        self.hand = Hand(starter_deck)
        self.score = 0

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
        for _ in range(index+1):
            card=next(iterable)
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
        draw_decision = action[0]
        if len(draw_deck) != 0 and len(discard_deck) != 0:
            if draw_decision > 0.5 or len(draw_deck) == 0:
                self.pickup_pile(discard_deck)
            else:
                self.draw_card(draw_deck)

        self.place_sets()

        discard_decision = round(action[1]*len(self.hand))
        self.discard(discard_decision, discard_deck)
        return len(self.hand)
