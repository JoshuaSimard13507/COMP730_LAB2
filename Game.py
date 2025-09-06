"""
File: src/Game.py
Implements the Game class for the Nim Problem.
Author: Joshua Simard
Created: 9/4/25
Developer: Joshua Simard
Date: 9/7/25

This module contains the Game class used to manage the state and rules of the NIM game.
"""

class Game:
    """
    Represents the state and rules of a NIM game.
    Manages scores, game type, and player list.
    """
    def __init__(self):
        """
        Initializes a new Game instance with default values.
        """
        self.target_score = None  # Optional: In Game Type 2, if players score below this value, they win.
        self.current_score = None
        self.game_type = None
        self.players = []

    def get_target_score(self):
        """
        Returns the target score for the game.
        """
        return self.target_score

    def set_target_score(self, score):
        """
        Sets the target score for the game.

        Args:
            score (int): The target score to set.
        """
        self.target_score = score

    def get_current_score(self):
        """
        Returns the current score of the game.
        """
        return self.current_score

    def set_current_score(self, score):
        """
        Sets the current score of the game.

        Args:
            score (int): The current score to set.
        """
        self.current_score = score

    def get_win_condition(self):
        """
        Determines if the win condition has been met based on the game type.

        Returns:
            bool: True if the win condition is met, False otherwise.
        """
        match self.game_type:
            case 1:
                return self.current_score <= 0
            case 2:
                return self.current_score <= self.target_score
            case 3:
                return self.current_score <= self.target_score

    def set_players(self, players):
        """
        Sets the list of players for the game.

        Args:
            players (list): List of Player objects.
        """
        self.players = players

    def get_players(self):
        """
        Returns the list of players in the game.
        """
        return self.players