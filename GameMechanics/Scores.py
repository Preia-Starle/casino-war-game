import sys
sys.path.append(".")

class Scores():
    """
    Keeps track of the scores of all players

    The player with the highest score is placed first,
    followed by the one with the second highest score, and so on
    """

    def __init__(self):
        """Initialize the Scores object with an empty leaderboard"""

        self.leaderboard = []


    def __str__(self):
        """returns a string containg the name and the score of each player"""

        return "\n".join(f"{name}: {score}" for name, score in self.leaderboard)


    def add_score(self, player_name, player_score):
        """saves the name and the score of the player inside the a dictionary"""

        # remove the the score of the player if it already exists in the leaderboard
        for i in range(len(self.leaderboard)):
            if self.leaderboard[i][0] == player_name:
                self.leaderboard.pop(i)
                break;

        # change the player's score
        self.__insert_score_ordered(player_name, player_score)

    def update_score(self, player_name, player_score):
        """ update player score, throws ValueError if the name does not exist """

        # go through the leaderboard and find the player 
        for i in range(len(self.leaderboard)):
            if self.leaderboard[i][0] == player_name:

                # change the player's score
                self.__insert_score_ordered(player_name, player_score)

                return self.leaderboard

        # raise an execption if the player wasn't found
        raise ValueError("Player name does noy exist")


    def __insert_score_ordered(self, player_name, player_score):
        """insert the player name and score in order"""

        # tuple that will be inserted into the leaderboard
        elt = (player_name, player_score)

        index = 0

        # increment the index if the score inside of the leaderboard is greater that the player_score
        while index < len(self.leaderboard) and player_score <= self.leaderboard[index][1]:
            index += 1

        self.leaderboard.insert(index, elt)

    def get_list_of_scores(self):
        return self.leaderboard

if __name__ == "__main__":
    h = Scores()

    h.add_score("Kate", 3000)
    h.add_score("Antoine", 2000)
    h.add_score("Tibor", 1000)
    h.add_score("Antoine", 1500)

    print(h)

