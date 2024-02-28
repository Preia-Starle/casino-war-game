
class Player():
    # player selected nickname
    nickname = ""
    balance = 0

    # dictionary value: player nickname, key: balance
    players = {}

    """ initialise player object """
    def __init__(self, nickname, balance=0):
        self.nickname = nickname
        self.balance = balance
        # add player to dictionary with initial balance
        self.players[nickname] = balance


    """ add new player to players """
    @classmethod
    def addPlayer(cls, nickname, balance=0):
        if nickname not in cls.players:
            cls.players[nickname] = balance
    
    """ update player balance after gain/loss """
    @classmethod
    def updateBalance(cls, nickname, newBalance):
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




