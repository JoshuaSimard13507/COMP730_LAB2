"""
File: src/Player.py
Implements the Player class for the Nim Problem.
Author: Joshua Simard
Created: 9/4/25
Developer: Joshua Simard
Date: 9/7/25

This module contains the Player class used to represent a player in the NIM game.
"""

class Player:
    """
    Represents a player in the NIM game.
    Stores the player's name and score.
    """
    def __init__(self, name):
        """
        Initializes a new Player instance.

        Args:
            name (str): The name of the player.
        """
        self.name = name

    def get_name(self):
        """
        Returns the player's name.

        Returns:
            str: The name of the player.
        """
        return self.name

    def set_name(self, name):
        """
        Sets the player's name.

        Args:
            name (str): The new name for the player.
        """
        self.name = name