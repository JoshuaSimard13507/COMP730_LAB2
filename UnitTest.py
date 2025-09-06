"""
File: src/UnitTest.py
Unit tests for the NIM game implementation.
Author: Joshua Simard
Created: 9/7/25
Developer: Joshua Simard
Date: 9/7/25

This module contains unit tests for the Game and Player classes.
"""

import unittest
from Game import Game
from Player import Player

class TestPlayer(unittest.TestCase):
    """
    Unit tests for the Player class.
    """
    def test_player_name(self):
        """
        Tests getting and setting the player's name.
        """
        player = Player("Alice")
        self.assertEqual(player.get_name(), "Alice")
        player.set_name("Bob")
        self.assertEqual(player.get_name(), "Bob")

    def test_player_score(self):
        """
        Tests getting and setting the player's score.
        """
        player = Player("Alice")
        self.assertEqual(player.get_score(), 0)
        player.set_score(5)
        self.assertEqual(player.get_score(), 5)

class TestGame(unittest.TestCase):
    """
    Unit tests for the Game class.
    """
    def setUp(self):
        """
        Sets up a Game instance and players for testing.
        """
        self.game = Game()
        self.players = [Player("Alice"), Player("Bob")]
        self.game.set_players(self.players)

    def test_set_and_get_target_score(self):
        """
        Tests setting and getting the target score.
        """
        self.game.set_target_score(10)
        self.assertEqual(self.game.get_target_score(), 10)

    def test_set_and_get_current_score(self):
        """
        Tests setting and getting the current score.
        """
        self.game.set_current_score(21)
        self.assertEqual(self.game.get_current_score(), 21)

    def test_get_players(self):
        """
        Tests retrieving the list of players.
        """
        self.assertEqual(len(self.game.get_players()), 2)
        self.assertEqual(self.game.get_players()[0].get_name(), "Alice")

    def test_win_condition_type_1(self):
        """
        Tests win condition logic for game type 1.
        """
        self.game.game_type = 1
        self.game.set_current_score(0)
        self.assertTrue(self.game.get_win_condition())
        self.game.set_current_score(1)
        self.assertFalse(self.game.get_win_condition())

    def test_win_condition_type_2(self):
        """
        Tests win condition logic for game type 2.
        """
        self.game.game_type = 2
        self.game.set_current_score(5)
        self.game.set_target_score(5)
        self.assertTrue(self.game.get_win_condition())
        self.game.set_current_score(6)
        self.assertFalse(self.game.get_win_condition())

    def test_win_condition_type_3(self):
        """
        Tests win condition logic for game type 3.
        """
        self.game.game_type = 3
        self.game.set_current_score(2)
        self.game.set_target_score(2)
        self.assertTrue(self.game.get_win_condition())
        self.game.set_current_score(3)
        self.assertFalse(self.game.get_win_condition())

if __name__ == "__main__":
    unittest.main()