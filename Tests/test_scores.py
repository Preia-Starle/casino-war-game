import sys
sys.path.append(".")
from GameMechanics.Scores import Scores
from Players.Player import Player

import unittest

class TestScores(unittest.TestCase):

    def test_init_default_object(self):
        """Test the add_player() method from the Scores class"""
        scores = Scores()

        res = scores
        exp = Scores
        self.assertIsInstance(res, exp)

    def test_str_method(self):
        """Test the __str__() method from the Scores class"""
        scores = Scores()

        res = str(scores)
        exp = f""
        self.assertEqual(res, exp)

    def test_add_player(self):
        """Test the add_player() method from the Scores class"""
        scores = Scores()

        # adding one player
        scores.add_player(Player("player1"))
        res = scores.leaderboard
        exp = [Player("player1")]
        self.assertEqual(res, exp)

        # adding another player with a smaller balance
        scores.add_player(Player("player2"))
        res = scores.leaderboard
        exp = [Player("player1"), Player("player2")]
        self.assertEqual(res, exp)

        # adding the same player
        scores.add_player(Player("player1"))
        res = scores.leaderboard
        exp = [Player("player2"), Player("player1")]
        self.assertEqual(res, exp)

    def test_update_player_balance(self):
        """Test the update_player_balance() method from the Scores class"""
        scores = Scores()

        
        scores.add_player(Player("player1", 1000))
        scores.update_player_balance(Player("player1", 1000), 500)

        res = scores.leaderboard[0].balance
        exp = 500
        self.assertEqual(res, exp)

    def test_equal_method(self):
        """Test the __eq__() method from the Scores class"""
        scores = Scores()

        # when the objects are the same
        test_obj = Scores()
        res = scores == test_obj
        exp = True
        self.assertEqual(res, exp)

        # when the objects are different
        test_obj = Scores()
        test_obj.add_player(Player("player1"))
        res = scores == test_obj
        exp = False
        self.assertEqual(res, exp)

        # when the objects are of different type
        test_obj = Player("player1")
        res = scores == test_obj
        exp = False
        self.assertEqual(res, exp)

    def test_get_names(self):
        scores = Scores()
        scores.add_player(Player("player1"))
        scores.add_player(Player("player2"))

        res = scores.get_names()
        exp = ["player1", "player2"]
        self.assertEqual(res, exp)

        


