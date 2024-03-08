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

        # testing
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

        # testing
        res = ai.getOccurrences(shuffled_deck)
        self.assertEqual(len(res), 13)

    def test_calculate_probabilities(self):
        """Test the calculateProbabilites() method of the Intelligence class"""
        # initialize
        cards = cardClass.Card()
        deck = deckClass.Deck(cards)
        shuffled_deck = deck.shuffleDeck()
        ai = Intelligence(shuffled_deck, 1000)

        # testing
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

        # testing
        res = ai.calculateTieProbability(shuffled_deck)
        self.assertIsInstance(res, float)

    def test_calculate_higher_card_probability(self):
        """Test the calculateHigherCardProbability() method of the Intelligence class"""
        # initialize
        cards = cardClass.Card()
        deck = deckClass.Deck(cards)
        shuffled_deck = deck.shuffleDeck()
        ai = Intelligence(shuffled_deck, 1000)

        # testing
        res = ai.calculateHigherCardProbability(shuffled_deck)
        self.assertIsInstance(res, float)

        self.assertEqual(0 < res < 100, True)

    def test_decide_surrender_medium_mode(self):
        """Test the decideSurrenderMediumMode() method of the Intelligence class"""
        # initialize
        cards = cardClass.Card()
        deck = deckClass.Deck(cards)
        shuffled_deck = deck.shuffleDeck()
        ai = Intelligence(shuffled_deck, 1000)

        # testing with shuffled_deck
        res = ai.decideSurrenderMediumMode(shuffled_deck)
        self.assertIsInstance(res, bool)

        # testing with different shuffled_deck
        shuffled_deck = deck.shuffleDeck()
        res = ai.decideSurrenderMediumMode(shuffled_deck)
        self.assertIsInstance(res, bool)
        
        

