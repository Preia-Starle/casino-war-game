import sys
sys.path.append(".")

import unittest
import random
from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass

class TestDeck(unittest.TestCase, cardClass.Card):

    def test__init__deck(self):
        """ Test constructor """
        # create test card object
        cardInstance = cardClass.Card()
        cardInstance.testCards = {
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
        cardInstance.testSuits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        # call the constructor and pass the test card object
        deckInstance = deckClass.Deck(cardInstance)
        # make sure deck and shuffledDeck properly initialised
        self.assertEqual(deckInstance.deck, {})
        self.assertEqual(deckInstance.shuffledDeck, {}) 
        # make sure card object with cards and suits gets successfully passed
        self.assertEqual(deckInstance.cards, cardInstance.testCards)
        self.assertEqual(deckInstance.suits, cardInstance.testSuits)


    def testCreateDeck(self):
        """Test create deck"""
         # create test card object
        cardInstance = cardClass.Card()
        cardInstance.testCards = {
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
        cardInstance.testSuits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        # call the constructor and pass the test card object
        deckInstance = deckClass.Deck(cardInstance)
        for cardName, cardValue in cardInstance.testCards.items():
            for suit in cardInstance.testSuits:
                deckInstance.deck[cardName + " of " + suit] = cardValue
        expectedOutput = deckInstance.deck
        methodOutput = deckInstance.createDeck()
        self.assertEqual(expectedOutput, methodOutput)

    
    def testShuffleDeck(self):
        """Test Shuffle deck"""
         # create test card object
        cardInstance = cardClass.Card()
        cardInstance.testCards = {
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
        cardInstance.testSuits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        # call the constructor and pass the test card object
        deckInstance = deckClass.Deck(cardInstance)
        deck = deckInstance.createDeck()
        listDeck = list(deck.items())

        random.shuffle(listDeck)
        deckInstance.shuffledDeck = dict(listDeck)
        expectedOutput = deckInstance.shuffledDeck

        methodOutput = deckInstance.shuffleDeck()
        self.assertEqual(expectedOutput, methodOutput)

