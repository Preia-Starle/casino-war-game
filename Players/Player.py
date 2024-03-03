import sys
sys.path.append(".")

from GameMechanics.Scores import Scores 

class Player():
    # player selected nickname
    nickname = ""
    balance = 0


    def __init__(self, nickname, scores:Scores, balance=0):
        """ initialise player object with Scores object """

        self.nickname = nickname
        self.balance = balance
        self.scores = scores

        # add player to scores with initial balance
        scores.add_score(self.nickname, self.balance)

    def __str__(self):
        """returns a string containg the name and the score of each player"""
        # get the __str__ method from the Scores class
        return str(self.scores)

    def addPlayer(self, nickname, balance=0):
        """ add new player to scores """

        self.scores.add_score(nickname, balance)
    
    def updateBalance(self, nickname, newBalance):
        """ update player balance after gain/loss, throws ValueError if the nickname does not exist """

        try:
            self.scores.update_score(nickname, newBalance)

        except ValueError as e:
            raise



if __name__ == "__main__":
    s = Scores()
    p = Player("Tibor", s, 0)
    p.updateBalance("Tibor", 350)
    p.addPlayer("Antoine")

    print(p)  




