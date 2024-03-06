import sys
sys.path.append(".")

import unittest
from CardMechanics import Card as cardClass
from CardMechanics import CardHand as cardHandClass
from CardMechanics import Deck as deckClass

class TestCardHand(unittest.TestCase, deckClass.Deck, cardClass.Card):

    def test__init__(self):
        """ Test constructor """
        # create test deck object
        testDeck = [(cardClass.Card(), "heart"), (cardClass.Card(), "diamond"), (cardClass.Card(), "club")]
        # create instance of the cardHand class, pass the test deck
        cardHandInstance = cardHandClass.CardHand(testDeck)
        # make sure empty dict for playerHand and aiHand created at object construction
        self.assertEqual(cardHandInstance.playerHand, {})
        self.assertEqual(cardHandInstance.aiHand, {}) 
        # make sure deck instance gets successfully passed
        self.assertEqual(cardHandInstance.shuffledDeck, testDeck)




if __name__ == '__main__':
    unittest.main()