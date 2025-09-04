"""
File: src/Main.py
Implements the main function of the Nim Problem.
Author: Joshua Simard
Created: 9/4/25
Developer: Joshua Simard
Date: 9/7/25

This module contains the main logic for presenting the NIM problem.
"""

from Game import Game
from Player import Player

def setup_game():
    player_count = input("How many players?")
    players = []
    for i in range(0, int(player_count)):
        players.append(Player())


def main():
    current_game = Game()
    game_over = False
    players



    while game_over != True:


if __name__ == "__main__":
    main()