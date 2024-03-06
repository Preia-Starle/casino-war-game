import sys
sys.path.append(".")


class Player():
    """
    Player has a name and a balance
    """

    def __init__(self, nickname,  balance=1000):
        """ initialise player object """

        self.nickname = nickname
        self.balance = balance


    def __str__(self):
        """ returns a string containg the name and the score of the player """
        return f"{self.nickname} -- {self.balance:,d}$"
    

    def update_balance(self, new_balance):
        """ set new balance """
        self.balance = new_balance


    def get_balance(self):
        return self.balance


    def get_name(self):
        return self.nickname


if __name__ == "__main__":
    p = Player("Antoine", 0)
    p.update_balance(50000)

    print(p)  




