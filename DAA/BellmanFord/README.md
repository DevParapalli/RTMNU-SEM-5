# Bellman Ford

Title: Design and Analysis of Algorithms Practical - Bellman-Ford Algorithm Implementation for Shortest Path

Introduction:
The Bellman-Ford algorithm is a fundamental graph algorithm used to find the shortest path from a source vertex to all other vertices in a weighted graph. It is a dynamic programming-based algorithm that can handle graphs with negative edge weights, making it a versatile choice for various real-world applications such as network routing, distance-vector routing protocols, and more. In this practical, we will implement the Bellman-Ford algorithm and analyze its time complexity.

Objective:
The main objective of this practical is to understand the Bellman-Ford algorithm, implement it in a programming language (e.g., Python, C++), and analyze its time complexity. Students will gain hands-on experience in designing and coding an essential algorithm for solving the single-source shortest path problem.

Implementation:

Step 1: Initialize
- Create a data structure to represent the graph. You can use an adjacency list or adjacency matrix, depending on your preference.
- Initialize an array to store the distance from the source vertex to all other vertices. Set the distance of the source vertex to 0 and all other vertices to infinity.
- Initialize an array to store the predecessor (previous vertex) for each vertex.
- Create a loop to iterate through all vertices V-1 times, where V is the number of vertices in the graph. This loop will help in relaxing edges to find the shortest path.

Step 2: Relaxation
- In each iteration of the loop, iterate through all edges of the graph and relax them. Relaxing an edge means checking if the current distance to a vertex can be reduced by considering the edge.
- To relax an edge (u, v) with weight w, check if the distance to vertex v (distance[v]) can be minimized by taking the path through vertex u (distance[u] + w).
- If the above condition is satisfied, update the distance[v] to the new minimum value (distance[u] + w) and update the predecessor of vertex v to u.

Step 3: Detection of Negative Cycles
- After V-1 iterations (where V is the number of vertices), if there are still updates occurring during the relaxation step, it indicates the presence of a negative cycle in the graph. This is because in a graph with V vertices, the shortest path cannot have more than V-1 edges.
- If a negative cycle is detected, the Bellman-Ford algorithm can be used to detect and report it.

Step 4: Output
- After completing V-1 iterations, you will have the shortest distance from the source vertex to all other vertices, and you can reconstruct the shortest paths using the predecessor information.

Complexity Analysis:

1. Time Complexity:
   - The Bellman-Ford algorithm performs relaxation for each edge V-1 times, where V is the number of vertices. In the worst case, it results in a time complexity of O(V * E), where E is the number of edges.
   - However, with some optimizations, such as early termination if no updates occur in an iteration, the algorithm's performance can be improved.

2. Space Complexity:
   - The space complexity is O(V), where V is the number of vertices, due to the arrays used to store distance and predecessor information.

Conclusion:
The Bellman-Ford algorithm is a versatile algorithm for finding the shortest paths in a weighted graph. This practical exercise provides students with a hands-on experience in implementing and analyzing the algorithm's time complexity. Understanding and implementing such fundamental algorithms is essential for anyone studying the design and analysis of algorithms.
