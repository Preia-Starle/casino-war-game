import sys
sys.path.append(".")

class HighScore():

    def __init__(self):
        """Initialize the HighScore object with an empty leaderboard"""

        self.leaderboard = []


    def __str__(self):
        """returns a list of strings containg the name and the score"""
        return "\n".join(f"{name}: {score}" for name, score in self.leaderboard)


    def save_score(self, player_name, player_score):
        """saves the name and the score of the player inside the a dictionary"""

        # remove the the score of the player if it already exists in the leaderboard
        for i in range(len(self.leaderboard)):
            if self.leaderboard[i][0] == player_name:
                self.leaderboard.pop(i)
                break;

        self.insert_score_ordered(player_name, player_score)


    def insert_score_ordered(self, player_name, player_score):
        """insert the player name and score in order"""

        # tuple that will be inserted into the leaderboard
        elt = (player_name, player_score)

        index = 0

        # increment the index if the score inside of the leaderboard is greater that the player_score
        while index < len(self.leaderboard) and player_score <= self.leaderboard[index][1]:
            index += 1

        self.leaderboard.insert(index, elt)
        


h = HighScore()

h.save_score("Kate", 3000)
h.save_score("Antoine", 2000)
h.save_score("Tibor", 1000)
h.save_score("Antoine", 1500)

print(h)

