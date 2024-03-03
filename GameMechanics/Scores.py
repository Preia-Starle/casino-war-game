import sys
sys.path.append(".")

from Players.Player import Player

class Scores():
    """
    Keeps track of all the players

    The player with the highest score is placed first,
    followed by the one with the second highest score, and so on

    Saves Player objects inside a list
    """

    def __init__(self):
        """Initialize the Scores object with an empty leaderboard"""

        # stores player objects
        self.leaderboard = []


    def __str__(self):
        """returns a string containg the name and the score of each player"""

        # use Player's __str__ method
        return "\n".join([str(p) for p in self.leaderboard])


    def add_player(self, player:Player):
        """add new player, update the player if he already exists"""

        # try to update the balance of the player
        try:
            self.update_player_balance(player, player.get_balance())

        # add new player if he doesn't exist
        except ValueError:
            self.__insert_score_ordered(player)


    def update_player_balance(self, player:Player, score:int):
        """updates the score of the player object and places him accordingly in the list"""

        # search for player in the leaderboard
        for p in self.leaderboard:
            if p == player:

                p.update_balance(score)

                # remove the player and add him back again
                # in order to get the right order
                self.leaderboard.remove(p)
                self.__insert_score_ordered(p)

                return p

        # raise an execption if the player wasn't found
        raise ValueError("Player name does noy exist")



    def __insert_score_ordered(self, player:Player):
        """insert the player in the leaderboard in the right order (from the largest balance to the lowest one)"""

        player_score = player.get_balance()
        player_name = player.get_name()

        index = 0

        # increment the index if the score inside of the leaderboard is greater that the player_score
        while index < len(self.leaderboard) and player_score <= self.leaderboard[index].get_balance():
            index += 1

        # insert the player when the right place was found
        self.leaderboard.insert(index, player)

    def get_names(self):
        """ returns list of all names """
        return [p.get_name() for p in self.leaderboard]


if __name__ == "__main__":

    a = Player("Antoine", 500)
    t = Player("Tibor", 1000)
    k = Player("Kate", 1500)


    h = Scores()
    h.add_player(a)
    h.add_player(k)
    h.add_player(t)
    h.update_player_balance(a, 2000)

    print(h)

