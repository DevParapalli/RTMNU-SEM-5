from heapq import heappop, heappush
from typing import Literal

def solve_8_puzzle(initial_state: list[list[int]]):
    # Define the goal state
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # Define the Manhattan distance heuristic function
    def heuristic(state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    row = (state[i][j] - 1) // 3
                    col = (state[i][j] - 1) % 3
                    distance += abs(row - i) + abs(col - j)
        return distance

    # Define the A* algorithm
    def astar():
        open_set = []
        heappush(open_set, (heuristic(initial_state), 0, initial_state, []))
        closed_set = set()

        while open_set:
            _, cost, current_state, path = heappop(open_set)
            if current_state == goal_state:
                return path

            closed_set.add(tuple(map(tuple, current_state)))

            for move in get_possible_moves(current_state):
                new_state = apply_move(current_state, move)
                if tuple(map(tuple, new_state)) not in closed_set:
                    new_cost = cost + 1
                    new_path = path + [move]
                    heappush(open_set, (new_cost + heuristic(new_state), new_cost, new_state, new_path))

    # Helper functions
    def get_possible_moves(state: list[list[int]]) -> list[Literal['U', 'D', 'L', 'R']]:
        # Returns a list of possible moves (up, down, left, right)
        
        # Find the position of the empty tile
        row = -1
        col = -1
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    row = i
                    col = j
                    break
        if row == -1 or col == -1:
            raise Exception('Invalid state')
        # Check if the empty tile can move up, down, left, or right
        moves = []
        if row > 0:
            moves.append('U')
        if row < 2:
            moves.append('D')
        if col > 0:
            moves.append('L')
        if col < 2:
            moves.append('R')
        return moves

    def apply_move(state: list[list[int]], move: Literal['U', 'D', 'L', 'R']):
        # Applies the given move to the state and returns the new state
        row = -1
        col = -1
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    row = i
                    col = j
                    break
        if row == -1 or col == -1:
            raise Exception('Invalid state')
        
        new_state = [row[:] for row in state]
        
        if move == 'U':
            new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]
        elif move == 'D':
            new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]
        elif move == 'L':
            new_state[row][col], new_state[row][col - 1] = new_state[row][col - 1], new_state[row][col]
        elif move == 'R':
            new_state[row][col], new_state[row][col + 1] = new_state[row][col + 1], new_state[row][col]

        return new_state
    
    
    # Call the A* algorithm
    solution = astar()
    return solution

def main():
    initial_state = [[7, 3, 1],
                     [4, 8, 6],
                     [2, 5, 0]]
    solution = solve_8_puzzle(initial_state)
    print(solution)

if __name__ == '__main__':
    main()