import sys
sys.path.append(".")

from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass

class CardHand(deckClass.Deck):

    """Initialize CardHand object"""
    def __init__(self, deck):
        self.playerHand = {}
        self.AiHand = {}

        self.shuffledDeck = deck.shuffleDeck()

    """Draws one card for the player and one for the AI and removes those cards from the deck"""
    def drawCard(self):
        print("Original Deck: ", self.shuffledDeck)
        self.playerHand = self.shuffledDeck.popitem()
        self.AiHand = self.shuffledDeck.popitem()
        print("Player Hand: ", self.playerHand, "\nAi Hand: ", self.AiHand)
        print("Deck after the two draws: ", self.shuffledDeck)


c = cardClass.Card()
d = deckClass.Deck(c)
ch = CardHand(d)
ch.drawCard()

    