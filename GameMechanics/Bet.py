import sys
sys.path.append(".")

class Bet():

    betPlayer = 0
    betAi = 0

    totalBalancePlayer = 0
    totalBalanceAi = 0

    """ update balance if win """
    def cardHigher(self, currentBalance, bet):
        # if card higher (win) -> win double the bet
        currentBalance += 2* bet
        return currentBalance

    """ update balance if loss """
    def cardLower(self, currentBalance, bet):
        # if card lower (loss) -> loss of the bet
        currentBalance -= bet
        return currentBalance
    
    """ update balance if surrender decision occurs """
    def surrend(self, currentBalance, bet):
        # loss of half of the bet in case decision to surrender
        currentBalance -= bet/2
        return currentBalance

    """ add stakes when decision to go to war occurs """
    def war(self, bet):
        # double the stakes in case decision to go to war
        bet += bet
        return bet
