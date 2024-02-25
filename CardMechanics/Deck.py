import random
import sys
sys.path.append(".")
from CardMechanics import Card as cardClass

class Deck(cardClass.Card):

    """Initialize Deck object"""
    def __init__(self, card):
        self.deck = {}
        self.shuffledDeck = {}

        self.cards = card.cards
        self.suits = card.suits


    """Create deck"""
    def createDeck(self):
        for cardName, cardValue in self.cards.items():
            for suit in self.suits:
                self.deck[cardName + " of " + suit] = cardValue
        return self.deck

    """Shuffle deck"""
    def shuffleDeck(self):
        deck = self.createDeck()
        listDeck = list(deck.items())

        random.shuffle(listDeck)
        self.shuffledDeck = dict(listDeck)
        return self.shuffledDeck

    def burnCard():
        pass

    