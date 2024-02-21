from Card import Card
from Deck import Deck

class CardHand(Deck):

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


c = Card()
d = Deck(c)
ch = CardHand(d)
ch.drawCard()

    