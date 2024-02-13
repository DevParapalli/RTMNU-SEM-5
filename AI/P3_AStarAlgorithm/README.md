# P3_AStarAlgorithm

A* (pronounced "A star") is a popular pathfinding algorithm used in computer science and artificial intelligence to find the shortest path between two nodes in a graph. It is often employed in navigation systems, video games, robotics, and various optimization problems.

The main goal of the A* algorithm is to efficiently navigate through a graph, considering the cost of moving from one node to another, while also taking into account an estimate of the remaining cost to reach the goal. It combines the characteristics of two other algorithms, Dijkstra's algorithm and Best-First Search, to achieve a balance between completeness and efficiency.

Here's how the A* algorithm works:

1. **Initialization:** Start with a graph representing the environment, where nodes represent locations and edges represent possible connections between locations. Assign a "start" node and a "goal" node.

2. **Open List:** Create an open list that will hold the nodes to be explored. Initially, only the start node is in this list.

3. **Closed List:** Create a closed list to keep track of nodes that have been visited and explored.

4. **Heuristic Function:** Define a heuristic function, denoted as h(n), which estimates the cost to reach the goal from a given node n. This is often an admissible (underestimating) heuristic, meaning it never overestimates the actual cost.

5. **Cost Function:** Assign a cost to move from one node to another. This can be the actual cost (e.g., distance between nodes) or an arbitrary value.

6. **Main Loop:** While the open list is not empty:
   - Select the node from the open list that has the lowest cost f(n) = g(n) + h(n), where g(n) is the cost to reach node n from the start.
   - If the selected node is the goal, the path has been found.
   - Otherwise, move the selected node from the open list to the closed list.
   - Expand the selected node by considering its neighboring nodes.
     - For each neighbor:
       - If the neighbor is in the closed list, skip it.
       - If the neighbor is not in the open list, calculate its g(n) and h(n) values, and add it to the open list.
       - If the neighbor is already in the open list, compare the new g(n) value to the existing one. If the new value is lower, update the node's information in the open list.

7. **Path Reconstruction:** Once the goal is reached, the shortest path can be reconstructed by following the parent pointers from the goal node back to the start node.

A* combines the advantages of Dijkstra's algorithm, which ensures that the shortest path is found, and Best-First Search, which is faster but might not find the optimal path. The use of the heuristic function guides the search towards the goal, improving efficiency.

However, it's important to note that the efficiency of A* depends heavily on the quality of the heuristic function. An admissible heuristic is crucial for guaranteeing optimality, but a more informed heuristic can significantly speed up the search process.

## Files

- [main.min.py](./main.min.py) - Minified without external comments
- [main.py](./main.py)