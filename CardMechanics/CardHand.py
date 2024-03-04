import sys
sys.path.append(".")

from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass

class CardHand(deckClass.Deck):

    """Initialize CardHand object"""
    def __init__(self, deck):
        self.playerHand = {}
        self.aiHand = {}
        self.shuffledDeck = deck

    """Draws one card for the player and one for the AI and removes those cards from the deck"""
    def drawCard(self, deck):
        self.playerHand = deck.popitem()
        self.aiHand = deck.popitem()
        currentDeck = deck
        
        return self.playerHand, self.aiHand, currentDeck

    
    """Gets the current deck"""
    @staticmethod
    def getShuffledDeck(self):
        return self.shuffledDeck


    