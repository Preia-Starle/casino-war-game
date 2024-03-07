import sys
sys.path.append(".")

import unittest
from CardMechanics import Card as cardClass

class TestCard(unittest.TestCase):

    def test__init__card(self):
        """ Test constructor """
        # create test card object
        testCards = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 11,
            "Queen": 12,
            "King": 13,
            "Ace": 14}
        testSuits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        cardInstance = cardClass.Card()
        # make sure card object with cards and suits gets successfully passed
        self.assertEqual(cardInstance.cards, testCards)
        self.assertEqual(cardInstance.suits, testSuits)


    def testGetCards(self):
        """ Test cards are being returned """
        testCards = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 11,
            "Queen": 12,
            "King": 13,
            "Ace": 14}
        cardInstance = cardClass.Card()
        methodOutput = cardInstance.getCards()
        self.assertEqual(methodOutput, testCards)
    
    
    def testGetSuits(self):
        """ Test suits are being returned """
        testSuits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        cardInstance = cardClass.Card()
        methodOutput = cardInstance.getSuits()  
        self.assertEqual(methodOutput, testSuits)  

   
