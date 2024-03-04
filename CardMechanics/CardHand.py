import sys
sys.path.append(".")

from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass

class CardHand(deckClass.Deck):

    """Initialize CardHand object"""
    def __init__(self, deck):
        self.playerHand = {}
        self.aiHand = {}

        self.shuffledDeck = deck.shuffleDeck()

    """Draws one card for the player and one for the AI and removes those cards from the deck"""
    def drawCard(self):
        self.playerHand = self.shuffledDeck.popitem()
        self.aiHand = self.shuffledDeck.popitem()
        currentDeck = self.shuffledDeck
        
        return self.playerHand, self.aiHand, currentDeck

    
    """Gets the current deck"""
    @staticmethod
    def getShuffledDeck(self):
        return self.shuffledDeck


c = cardClass.Card()
d = deckClass.Deck(c)
ch = CardHand(d)
result = ch.drawCard()
d.burnCard(result[2])
ch.drawCard()

    