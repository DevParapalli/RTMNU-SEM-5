# P2_TicTacToe

Tic Tac Toe is a popular two-player paper-and-pencil game played on a 3x3 grid. The players take turns to place their marks (traditionally "X" for one player and "O" for the other) on the empty cells of the grid. The goal of the game is to get three of your marks in a row, either horizontally, vertically, or diagonally, before your opponent does. If all cells are filled and no player has three in a row, the game is a draw.

The practical is implemented using Minimax Algorithm without any modifications.

The Minimax Algorithm is a decision-making algorithm commonly used in games with perfect information, like Tic Tac Toe. It is a recursive algorithm that searches through the game tree to determine the best move for a player in a given state. The name "Minimax" comes from the two key concepts it considers:

1. Minimize: The algorithm assumes that the opponent will play optimally, trying to minimize the player's gain.
2. Maximize: The algorithm also assumes that the player will play optimally, trying to maximize their own gain.

The Minimax Algorithm generates a tree of all possible game states (each node representing a board configuration) and assigns a value to each leaf node based on whether it leads to a win, loss, or draw. The algorithm then works its way back up the tree, propagating the values of the leaf nodes to the parent nodes using the following rules:

- If it's the player's turn, the parent node's value is the maximum of its children's values (because the player wants to maximize their advantage).
- If it's the opponent's turn, the parent node's value is the minimum of its children's values (because the opponent wants to minimize the player's advantage).

By applying this process recursively, the algorithm eventually reaches the root node, where it can choose the best move for the current player based on the values assigned to its children.

Using the Minimax Algorithm, the AI can determine the best move to make in Tic Tac Toe and ensure it plays optimally, never losing against a perfect opponent. However, the algorithm can be computationally expensive for larger game boards or more complex games, which is why more advanced techniques and optimizations like alpha-beta pruning are often used to speed up the search process.
