#! /usr/bin/env python
"""Maze Solver with DFS Algorithm"""

__author__ = "Devansh Parapalli"

 

MAZE = [[1,3,1,0,1,0,1,0,0,0,0,1,1,0,0],
        [1,0,1,0,1,0,1,0,1,0,0,1,0,0,0],
        [1,0,0,0,1,0,0,0,1,0,0,0,0,1,0],
        [1,0,1,0,1,1,0,1,1,1,1,1,0,1,0],
        [1,0,1,0,1,0,0,1,0,0,1,0,0,1,0],
        [1,1,1,0,1,0,0,0,0,0,1,0,0,1,0],
        [1,0,0,0,1,0,0,0,1,0,1,1,1,0,0],
        [1,0,1,1,1,1,1,1,1,0,1,0,0,0,0],
        [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
        [1,0,0,0,0,1,1,0,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,0,1,0,0,0,0,0,0,2],]
# 0 = Empty Space; 1 = Wall; 2 = Goal; 3 = Start

MOVE_MAP = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_valid_move(maze:list[list[int]], pos: tuple[int, int], result: list[list[int]]):
    """Checks if the move is valid"""
    if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(maze) and pos[1] < len(maze[0]) and maze[pos[0]][pos[1]] in [0, 2, 3] and result[pos[0]][pos[1]] == 0:
        return True
    return False
    
def solve_maze(maze: list[list[int]], current_pos: tuple[int, int], goal: tuple[int, int], result: list[list[int]]):
    if current_pos == goal:
        return True
    for move in MOVE_MAP:
        new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
        if is_valid_move(maze, new_pos, result):
            result[new_pos[0]][new_pos[1]] = 1
            if solve_maze(maze, new_pos, goal, result):
                return True
            result[new_pos[0]][new_pos[1]] = 0
    return False

def generate_solution(maze: list[list[int]]):
    result = [[0 for _ in range(len(maze[i]))] for i in range(len(maze))]
    
    start = [0, 0]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 3:
                start = [i, j]
    print(f"{start=}")
    goal = [0, 0]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                goal = [i, j]
    print(f"{goal=}")
    if solve_maze(maze, tuple(start), tuple(goal), result):
        return result
    else:
        return "No Solution Found"
    
if __name__ == "__main__":
    res = generate_solution(MAZE)
    if isinstance(res, str):
        print(res)
    else:
        for i in range(len(res)):
            print(res[i])



