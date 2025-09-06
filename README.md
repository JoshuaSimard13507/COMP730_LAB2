# COMP730_LAB2

In this implementation of the NIM game, players take turns subtracting 1, 2, or 3 from a starting score. The game supports multiple modes, including a standard mode, a custom mode with user-defined scores, and a randomized target mode. The game is played by two or more players, and the winner is determined by reaching the target score according to the selected game mode.

## Usage
When running the program, you will be prompted to enter the number of players and their names. You can then select a game mode:
- **Standard:** First to reach 0 wins.
- **Custom:** First to reach a user-defined target score wins.
- **Randomized:** Target score is randomized and hidden from players.

On each turn, players will be prompted to subtract 1, 2, or 3 from the current score. The game continues until the win condition for the selected mode is met.

## Unit Tests
The unit tests can be run directly by executing the 'UnitTest.py' file. These tests verify that the game logic works correctly, including score updates, win conditions, and player turns.