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
import random

def setup_game():
    player_count = input("How many players?")
    players = []
    for i in range(0, int(player_count)):
        name = input(f"Enter name for Player {i+1}:")
        players.append(Player(name))
    
    print("Game modes:\n1. Standard: First to reach 0 wins.\n2. Custom: First to reach target score wins.\n2. Custom: Ending value is randomized and not displayed.")
    gtype = input("Select game mode (1, 2, or 3):")
    match (int(gtype)):
        case 1:
            game = Game()
            game.gameType = 1
            game.set_current_score(21) #Default starting score for Game Type 1
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
        case 3:
            game = Game()
            game.gameType = 2
            game.set_current_score(21)  # Default starting score
            randomized_target = random.randint(0, 5)
            game.set_target_score(randomized_target)
            game.set_players(players)
            return game

        case _:
            print("Invalid selection. Please choose 1, 2, or 3.")
            return setup_game()



def main():
    current_game = setup_game()
    game_over = False




    while game_over != True:
        for player in current_game.get_players():
            print(f"{player.get_name()}'s turn. Current score: {current_game.get_current_score()}")
            while True:
                try:
                    points = int(input("Enter points to subtract (1, 2, or 3): "))
                    if points in [1, 2, 3]:
                        break
                    else:
                        print("Invalid input. Please enter 1, 2, or 3.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            new_score = current_game.get_current_score() - points
            current_game.set_current_score(new_score)
            print(f"New score after {player.get_name()}'s turn: {current_game.get_current_score()}")

        if(current_game.get_win_condition() == True):
            game_over = True
            print(f"Game Over! {player.get_name()} wins!")

if __name__ == "__main__":
    main()