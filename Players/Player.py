
class Player():
    # player selected nickname
    nickname = ""
    balance = 0


    def __init__(self, nickname, scores:Scores, balance=0):
    """ initialise player object with Scores object """

        self.nickname = nickname
        self.balance = balance
        self.scores = scores

        # add player to dictionary with initial balance
        scores.add
        self.players[nickname] = balance


    @classmethod
    def addPlayer(cls, nickname, balance=0):
    """ add new player to players """

        if nickname not in cls.players:
            cls.players[nickname] = balance
    
    @classmethod
    def updateBalance(cls, nickname, newBalance):
    """ update player balance after gain/loss """

        # if nickname exists in players dict
        if nickname in cls.players:
            # update balance
            cls.players[nickname] = newBalance
        # if not add him
        else:
            cls.addPlayer(nickname, newBalance)

        return cls.players

p = Player("Tibor", 0)
p.updateBalance("Tibor", 350)
print(Player.players)  




