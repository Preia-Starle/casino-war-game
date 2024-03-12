import sys
sys.path.append(".")

import unittest
from GameMechanics import Bet as betClass

class TestBet(unittest.TestCase):

    def testCardHigher(self):
        """ Test if balance updated after win """
        # assign test values
        currentBalance = 1000
        bet = 10
        # if card higher (win) -> win double the bet
        expectedBalance = currentBalance + bet
        # instantiate class
        betInstance = betClass.Bet()
        # call the method from the class
        updatedBalance = betInstance.cardHigher(currentBalance, bet)
        # make sure the expected balance and class method output same
        self.assertEqual(updatedBalance, expectedBalance)

    def testCardLower (self):
        """ Test if balance updated after loss """
        # assign test values
        currentBalance = 1000
        bet = 10
        # if card higher (win) -> win double the bet
        expectedBalance = currentBalance - bet
        # instantiate class
        betInstance = betClass.Bet()
        # call the method from the class
        updatedBalance = betInstance.cardLower(currentBalance, bet)
        # make sure the expected balance and class method output same
        self.assertEqual(updatedBalance, expectedBalance)

    def testSurrend(self):
        """ Test if balance updated after surrender decision occurs """
        # assign test values
        currentBalance = 1000
        bet = 10
        # loss of half of the bet in case decision to surrender
        expectedBalance = currentBalance - (bet/2)
        # instantiate class
        betInstance = betClass.Bet()
        # call the method from the class
        updatedBalance = betInstance.surrend(currentBalance, bet)
        # make sure the expected balance and class method output same
        self.assertEqual(updatedBalance, expectedBalance)

    def testWar(self):
        """ Test if bet updated if decision to go to war occurs """
        # assign test values
        bet = 10
        # loss of half of the bet in case decision to surrender
        expectedOutput = 2*bet
        # instantiate class
        betInstance = betClass.Bet()
        # call the method from the class
        updatedBet = betInstance.war(bet)
        # make sure the expected balance and class method output same
        self.assertEqual(updatedBet, expectedOutput)

    def testEnoughBalance(self):
        """ Test that check that the bet is not higher than the balance works """
        # assign test values
        currentBalance = 1000
        bet = 10
        hasEnoughBalance = False
        # if bet bet smaller than balance assign true else false
        if(bet <= currentBalance):
            hasEnoughBalance = True
        else:
            hasEnoughBalance = False
        expectedOutput = hasEnoughBalance
        # instantiate class
        betInstance = betClass.Bet()
        # call the method from the class
        classMethodOutput = betInstance.enoughBalance(bet, currentBalance)
        # make sure the expected balance and class method output same
        self.assertEqual(classMethodOutput, expectedOutput)

    def testGoAllInBoolean(self):
        """ Test go all in if player bet larger than ai balance returns correct boolean """
        betPlayer = 30
        aiBalance = 500
        if(betPlayer > aiBalance):
            goAllIn = True
        else:
            goAllIn = False
        expectedOutput = goAllIn
        # instantiate class
        betInstance = betClass.Bet()
        # call the method from the class
        *_, booleanOutput = betInstance.goAllIn(aiBalance, betPlayer)
        # make sure the expected balance and class method output same
        self.assertEqual(booleanOutput, expectedOutput)
    
    def testGoAllInBetUpdate(self):
        """ Test that aiBet updated to go all in if player bet larger than ai balance """
        betPlayer = 30
        aiBalance = 20
        if(betPlayer > aiBalance):
            aiBet = aiBalance
        else:
            aiBet = betPlayer
        expectedOutput = aiBet
        # instantiate class
        betInstance = betClass.Bet()
        # call the method from the class
        classMethodOutput,*_ = betInstance.goAllIn(betPlayer, aiBalance)
        # make sure the expected balance and class method output same
        self.assertEqual(classMethodOutput, expectedOutput)


        
    