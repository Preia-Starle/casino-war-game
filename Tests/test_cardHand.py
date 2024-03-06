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


    
    def testDrawCard(self):
        """Test Draws one card for the player and one for the AI and removes those cards from the deck"""
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


    def testEnoughCardsInDeck(self):
        """ Test check if enough cards in the deck to continue playing """
        playerHand = (cardClass.Card(), "heart")
        aiHand = (cardClass.Card(), "heart")
        # create test deck object
        testDeck = [(cardClass.Card(), "heart"), (cardClass.Card(), "diamond"), (cardClass.Card(), "club")]
        currentDeck = testDeck
        # in case of a tie
        if(playerHand == aiHand):
            # if there is less cards than 5
            if(len(currentDeck) < 5):
                # not enough cards in deck
                isEnoughCardsInDeck = False
            else:
                # enough cards in deck
                isEnoughCardsInDeck = True
        elif(len(currentDeck) < 2):
            # not enough cards in deck
            isEnoughCardsInDeck = False
        else:
            isEnoughCardsInDeck = True
        # create instance of the cardHand class, pass the test deck copy
        cardHandInstance = cardHandClass.CardHand(testDeck.copy())
        methodOutput = cardHandInstance.enoughCardsInDeck(playerHand, aiHand, currentDeck)
        self.assertEqual(isEnoughCardsInDeck, methodOutput)




if __name__ == '__main__':
    unittest.main()