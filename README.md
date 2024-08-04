# Tic-Tac-Toe Game

## Description

This is a simple command-line Tic-Tac-Toe game implemented in Python. The game allows a human player to play against the computer. The computer makes random moves while the player selects their moves by entering the number corresponding to the available squares.

## Rules

- The game is played on a 3x3 grid.
- The player uses 'O' and the computer uses 'X'.
- The first move belongs to the computer, which places an 'X' in a random empty square.
- Players take turns placing their marks in empty squares.
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
- If all nine squares are filled and neither player has three in a row, the game ends in a tie.

#Example Gameplay
1  |  2  |  3
-------------
4  |  5  |  6
-------------
7  |  8  |  9

**************

1  |  2  |  X
-------------
4  |  5  |  6
-------------
7  |  8  |  9

Enter available place: 5

1  |  2  |  X
-------------
4  |  O  |  6
-------------
7  |  8  |  9
**************

1  |  2  |  X
-------------
4  |  O  |  6
-------------
X  |  8  |  9

Enter available place: 1

O  |  2  |  X
-------------
4  |  O  |  6
-------------
X  |  8  |  9

...

