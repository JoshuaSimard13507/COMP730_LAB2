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

    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_name(self):
        return self.name

    def set_name(self, inp):
        self.name = inp

    def get_score(self):
        return self.score

    def set_score(self, inp):
        self.score = inp