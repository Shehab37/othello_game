# Othello Game

![image](https://github.com/Shehab37/othello_game/assets/20583611/46f4f486-5f81-4389-a344-c5e449a7c63a)


This is a Python implementation of the classic Othello game. The game features a graphical user interface (GUI) built using the Tkinter library.

## link to game exe :

        https://drive.google.com/file/d/14GVPeLhiFdceKrFRul18ZRlz9KHaX0h9/view?usp=drive_link
        
## link to video :

        https://www.youtube.com/watch?v=1mGs1n3lhDQ

To run the game, navigate to the directory where the game code is located and run the following command:

        python tk_gui.py

This will launch the game GUI.

Our game is an integration of three classes:

1. **Othello GUI**: The GUI itself.
2. **Othello Game**: The game includes the board, scores, and other game-related functionalities.
3. **Othello AI**: Includes the supported algorithms and heuristics.

## Game Playing Supported Algorithms:

1. **Minimax Algorithm**: This algorithm is a decision-making algorithm commonly used in game playing. It explores all possible moves and their outcomes, selecting the move that leads to the best outcome for the player. While guaranteed to find the optimal move, it can be slow and computationally expensive.

2. **Alpha-Beta Pruning**: An optimization of the minimax algorithm, it reduces the number of nodes to explore. By pruning branches that are guaranteed to lead to worse outcomes, it significantly reduces the search space and improves performance.

3. **Iterative Deepening**: This algorithm determines the best move for the AI player through a series of depth-limited searches. It starts with a small depth limit and gradually increases it until a certain time limit is reached. This allows the AI player to explore deeper into the game tree without exceeding the time limit.

## Used Heuristics, Descriptions, and Benefits:

1. **Coin Parity**: Calculates the difference between the number of coins owned by the AI player and the opponent. It provides a simple measure of the AI player's advantage in the game.

2. **Mobility**: Calculates the difference between the number of valid moves available to the AI player and the opponent. It measures the AI player's ability to move around the board and capture opponent's coins.

3. **Corners**: Provides a bonus to the AI player for occupying the corner squares of the board. Corners are important strategic positions as they cannot be captured by the opponent.

4. **Stability**: Calculates the difference between the number of stable coins owned by the AI player and the opponent. Stable coins cannot be flipped by the opponent in the future. This heuristic encourages the AI player to create stable positions on the board.
