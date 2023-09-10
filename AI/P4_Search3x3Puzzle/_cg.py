class Puzzle8:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.blank_row, self.blank_col = self.find_blank_position()

    def find_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j
        return -1, -1

    def is_valid_move(self, move):
        row, col = self.blank_row, self.blank_col
        if move == 'up':
            return row > 0
        elif move == 'down':
            return row < 2
        elif move == 'left':
            return col > 0
        elif move == 'right':
            return col < 2

    def make_move(self, move):
        if not self.is_valid_move(move):
            return False

        row, col = self.blank_row, self.blank_col

        if move == 'up':
            self.state[row][col], self.state[row - 1][col] = self.state[row - 1][col], self.state[row][col]
        elif move == 'down':
            self.state[row][col], self.state[row + 1][col] = self.state[row + 1][col], self.state[row][col]
        elif move == 'left':
            self.state[row][col], self.state[row][col - 1] = self.state[row][col - 1], self.state[row][col]
        elif move == 'right':
            self.state[row][col], self.state[row][col + 1] = self.state[row][col + 1], self.state[row][col]

        self.blank_row, self.blank_col = self.find_blank_position()
        return True

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state])

# Example usage:
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
puzzle = Puzzle8(initial_state)
print(puzzle)

# Perform a move
if puzzle.make_move('left'):
    print("Move left:")
    print(puzzle)
else:
    print("Invalid move")
