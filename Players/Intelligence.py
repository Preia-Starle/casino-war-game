import sys
sys.path.append(".")

from CardMechanics import CardHand as cardHandClass
from CardMechanics import Deck as deckClass
from CardMechanics import Card as cardClass
import random
from collections import defaultdict

class Intelligence(cardHandClass.CardHand, deckClass.Deck): 

    """Initialize Ai player object"""
    def __init__(self, difficultyMode, deck):
        self.difficultyMode = difficultyMode
        self.deck = deck

    """ Get occurrences of each rank in the deck """
    def getOccurrences(self, currentDeck):
        # initiate default dictionary to provide a default value for key hat hasnt been seen before
        occurrences = defaultdict(int)
        # loop through the currentDeck and add one everytime the value occurs
        for card in currentDeck:
            # Get the rank from the dictionary value 
            rank = currentDeck[card]  
            # append number of occurrences as value
            occurrences[rank] += 1
        return occurrences
    
    """ Calculate probability of drawing each rank from the deck"""
    def calculateProbabilities(self, occurrences, currentDeck):
        # get occurrences
        totalCardscurrentDeck = len(currentDeck)
        # calculate probabilities of each rank being drawn from the currentDeck
        # save each rank and probability as a key, value pair in a dictionary
        probabilities = {}
        for rank, countOfOccurences in occurrences.items():
            probabilities[rank] = countOfOccurences / totalCardscurrentDeck
        return probabilities
    
    """ Calculate probability of a tie """
    def calculateTieProbability(self, currentDeck):
        # get occurrences
        occurrences = self.getOccurrences(currentDeck)
        # get probabilities of each outcome
        probabilities = self.calculateProbabilities(occurrences, currentDeck)
        # calculate tie probability
        tieProbability = 0
        for rank in probabilities:
             # formula: each outcome probability squared and sumed together
            tieProbability += probabilities[rank] ** 2
        return tieProbability
    
    """ Calculate probability of drawing a higher card then the opponent """
    def calculateHigherCardProbability(self, currentDeck):
        # formula: (100 - tieProbability)/2
        higherCardProbability = (100 - self.calculateTieProbability(currentDeck))/2
        return higherCardProbability


    """ Easy mode: randomize surrender decision"""
    def decideSurrenderEasyMode(self):
        surrender = False
        surrender = random.choice([True, False])
        return surrender
    
    """ Medium difficulty mode: base surrender decision on probability of drawing higher card"""
    def decideSurrenderMediumMode(self):
        surrender = False
        surrenderThreshold = 50
        # get current deck
        currentDeck = self.getShuffledDeck(d)
        # calculate probability of a tie: number of the same value cards present/number of outcomes(total cards)
        print(self.calculateTieProbability(currentDeck))
        # calculate probability of a higher card: (100 - probability of a tie)/2
        higherCardProbablity = self.calculateHigherCardProbability(currentDeck)
        print(higherCardProbablity)
        # if probability of drawing higher > probability of drawing lower => surrender False, else True
        if higherCardProbablity > surrenderThreshold:
            surrender = False
        else:
            surrender = True
        return surrender

    
c = cardClass.Card()
d = deckClass.Deck(c)
ch = cardHandClass.CardHand(d)
i = Intelligence("medium", d)
i.decideSurrenderMediumMode()
    
            
            



    



    

        



            
    
