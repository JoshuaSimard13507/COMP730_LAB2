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
    
    print("Game modes:\n1. Standard: First to reach 0 wins.\n2. Custom: First to reach target score wins.")
    gtype = input("Select game mode (1 or 2):")
    match (int(gtype)):
        case 1:
            game = Game()
            game.gameType = 1
            game.set_current_score(10) #Default starting score for Game Type 1
            game.set_target_score(0)
            game.set_players(players)
            return game
        case 2:
            game = Game()
            game.gameType = 2

            # Get starting score and target score from userm with input validation
            while True:
                starting_score = input("Enter starting score:")
                try:
                    starting_score = int(starting_score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for starting score.")
            while True:
                target_score = input("Enter target score:")
                try:
                    target_score = int(target_score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for target score.")

            game.set_current_score(int(starting_score))
            game.set_target_score(int(target_score))
            game.set_players(players)
            return game
        case _:
            print("Invalid selection. Please choose 1 or 2.")
            return setup_game()



def main():
    current_game = Game()
    game_over = False
    players



    while game_over != True:


        if(current_game.get_current_score() >= current_game.get_target_score()):
            game_over = True
            print("Game Over!")

if __name__ == "__main__":
    main()