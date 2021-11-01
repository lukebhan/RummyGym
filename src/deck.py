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
