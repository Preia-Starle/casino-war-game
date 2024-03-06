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


    """Test Draws one card for the player and one for the AI and removes those cards from the deck"""
    def testDrawCard(self):
        # create test deck object
        testDeck = {"heart": 2, "diamond": 3 ,"club": 5}
        # create test deck copy to retain the original object
        originalTestDeck = testDeck.copy()
        # create instance of the cardHand class, pass the test deck copy
        cardHandInstance = cardHandClass.CardHand(testDeck.copy())
        # draw card for player and ai
        expectedPlayerHand = originalTestDeck.popitem()
        expectedAiHand = originalTestDeck.popitem()
        # call the method from the class
        playerHandOutput, aiHandOutput, deckOutput = cardHandInstance.drawCard(testDeck.copy())
        # make sure the expected ouput from test and class method same
        self.assertEqual(playerHandOutput, expectedPlayerHand) 
        self.assertEqual(aiHandOutput, expectedAiHand)
        self.assertEqual(deckOutput,originalTestDeck)




if __name__ == '__main__':
    unittest.main()