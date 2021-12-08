# A player class. Contains the players hand as a state, along with their possible actions. 

from hand import Hand

class Player():
    def __init__(self, starterDeck, name=None, verbose=False):
        self.name = name
        self.hand = Hand(starterDeck)
        self.score = 0
        self.verbose = verbose

    def placeSets(self):
        scores, sets = self.hand.getSetScores()
        for score, setVal in zip(scores, sets):
            self.score += score
            for card in setVal:
                self.hand.removeCard(card)

    def getScore(self):
        return self.score

    def discard(self, index, discardDeck):
        if index >= len(self.hand):
            raise IndexError("Trying to discard a index that is not feasible")
        iterable = iter(self.hand)
        card = next(iterable)
        for i in range(1, index+1):
            card=next(iterable)
        if self.verbose:
            print(self.name + " Discards " + card)
        discardDeck.addCard(card)
        self.hand.removeCard(card)

    def pickupPile(self, discardDeck):
        length = len(discardDeck)
        if length == 1:
            # only one random card to draw
            card = discardDeck.drawRandom()
            self.hand.addCard(card)
            return
        iterable = iter(discardDeck)
        toDiscard = []
        for i in range(length//2):
            card = next(iterable)
            self.hand.addCard(card)
            toDiscard.append(card)
        for card in toDiscard:
            discardDeck.removeCard(card)

    def drawCard(self, drawDeck):
        card = drawDeck.drawRandom()
        self.hand.addCard(card)

    def getHand(self):
        return self.hand

    def takeTurn(self, action, drawDeck, discardDeck):
        if self.verbose:
            print(self.name + " Turn. Score is ", str(self.score))
        drawDecision = action[0]
        if len(drawDeck) != 0 or len(discardDeck) != 0:
            if drawDecision > 0.5 or len(drawDeck) == 0:
                if self.verbose:
                    print(self.name + " Picks up half the discard deck! (" + str(len(discardDeck)) + " cards)")
                self.pickupPile(discardDeck)
            else:
                self.drawCard(drawDeck)
                if self.verbose:
                    print(self.name + " Picks up a card from the draw pile!")

        self.placeSets()
        discardDecision = round(action[1]*(len(self.hand)-1))
        if (len(self.hand) != 0):
            self.discard(discardDecision, discardDeck)
        if self.verbose:
            print(self.name + "'s hand looks like:")
            print(self.hand)
        return len(self.hand)
