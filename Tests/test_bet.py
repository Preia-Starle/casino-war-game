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

        

        


if __name__ == '__main__':
    unittest.main()