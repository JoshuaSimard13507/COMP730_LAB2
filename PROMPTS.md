PROMPT: Generate a doc string for the player.py file in the style of the main.py file.
NOTE: I had already hand written the main.py docstring.
OUTPUT: 
"""
File: src/Player.py
Implements the Player class for the Nim Problem.
Author: Joshua Simard
Created: 9/4/25
Developer: Joshua Simard
Date: 9/7/25

This module contains the Player class used to represent a player in the NIM game.
"""

PROMPT: Update Game.py to PEP8 standard
NOTE: Naturally I haven't included the complete output, as that is the entire contents 
of the file Game.py. However, if you look backwards in the git commits, you can see 
that it has update from camel case to snake case.
OUTPUT:
        self.target_score = None  # Optional: In Game Type 2, if players score below this value, they win.
        self.current_score = None
        self.game_type = None
        self.players = []

PROMPT: Generate a UnitTest.py file for the files Game.py, main.py, and Player.py in the style of other files, including docstrings.
OUTPUT: (The contents of the UnitTest.py file)