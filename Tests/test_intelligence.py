import sys
sys.path.append(".")
from Players.Intelligence import Intelligence
from CardMechanics import CardHand as cardHandClass
from CardMechanics import Deck as deckClass
from CardMechanics import Card as cardClass

import unittest

class TestIntelligence(unittest.TestCase):
    def test_init_default_object(self):
        """Test the constructor of the Intelligence class"""
        # initialize
        cards = cardClass.Card()
        deck = deckClass.Deck(cards)
        ai = Intelligence(deck, 1000)

        res = ai
        exp = Intelligence
        self.assertIsInstance(res, exp)

    def test_occurrences(self):
        """Test the getOccurrences() method of the Intelligence class"""
        # initialize
        cards = cardClass.Card()
        deck = deckClass.Deck(cards)
        shuffled_deck = deck.shuffleDeck()
        ai = Intelligence(shuffled_deck, 1000)

        res = ai.getOccurrences(shuffled_deck)
        self.assertEqual(len(res), 13)

    def test_calculate_probabilities(self):
        """Test the calculateProbabilites() method of the Intelligence class"""
        # initialize
        cards = cardClass.Card()
        deck = deckClass.Deck(cards)
        shuffled_deck = deck.shuffleDeck()
        ai = Intelligence(shuffled_deck, 1000)

        occurrences = ai.getOccurrences(shuffled_deck)
        res = ai.calculateProbabilities(occurrences, shuffled_deck)
        self.assertEqual(len(res), 13)


    def test_calculate_probabilities(self):
        """Test the calculateTieProbability() method of the Intelligence class"""
        # initialize
        cards = cardClass.Card()
        deck = deckClass.Deck(cards)
        shuffled_deck = deck.shuffleDeck()
        ai = Intelligence(shuffled_deck, 1000)

        res = ai.calculateTieProbability(shuffled_deck)
        self.assertIsInstance(res, float)
        

