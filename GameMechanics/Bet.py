import sys
sys.path.append(".")

class Bet():


    def cardHigher(self, currentBalance, bet):
        """ Update balance if win """
        # if card higher (win) -> win double the bet
        currentBalance += bet 
        return currentBalance

    def cardLower(self, currentBalance, bet):
        """ Update balance if loss """
        # if card lower (loss) -> loss of the bet
        currentBalance -= bet
        return currentBalance
    
    def surrend(self, currentBalance, bet):
        """ Update balance if surrender decision occurs """
        # loss of half of the bet in case decision to surrender
        currentBalance -= bet/2
        return currentBalance

    def war(self, bet):
        """ Add stakes when decision to go to war occurs """
        # double the stakes in case decision to go to war
        bet += bet
        return bet

    def enoughBalance(self, bet, currentBalance):
        """ Check that the bet is not higher than the balance """
        hasEnoughBalance = False
        if(bet <= currentBalance):
            hasEnoughBalance = True
        else:
            hasEnoughBalance = False
        return hasEnoughBalance
    
    def goAllIn(self, aiBalance, betPlayer):
        """ Go all in if player bet larger than ai balance """
        aiBet = 0
        goAllIn = False
        if(betPlayer > aiBalance):
            aiBet = aiBalance
            goAllIn = True
        else:
            aiBet = betPlayer
            goAllIn = False
        return aiBet, goAllIn
        

