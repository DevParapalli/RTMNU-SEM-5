# Dijkstra

Title: Implementation of Dijkstra's Algorithm in an Undirected Graph

**Theory:**

**Introduction:**

Dijkstra's Algorithm, named after its creator Edsger W. Dijkstra, is a widely used algorithm for finding the shortest path between nodes in a weighted graph. It is particularly useful in various applications, such as network routing, GPS navigation, and optimizing transportation routes. This practical aims to implement Dijkstra's Algorithm to find the shortest path in an undirected graph.

**Algorithm Overview:**

Dijkstra's Algorithm operates on a weighted graph, where each edge has a non-negative weight associated with it. The main idea behind the algorithm is to maintain a set of visited nodes and a set of tentative distances from a source node to all other nodes. It iteratively selects the node with the smallest tentative distance and explores its neighbors, updating their tentative distances if a shorter path is found. This process continues until all nodes have been visited or until the destination node is reached.

The algorithm maintains two sets:
1. **Visited Set:** This set contains the nodes for which the shortest path from the source has already been determined.
2. **Unvisited Set:** This set contains the nodes for which the shortest path from the source is yet to be determined.

**Pseudocode:**

Here is the pseudocode for Dijkstra's Algorithm:

```plaintext
1. Create a set S that will contain the visited nodes, initially empty.
2. Create a set Q that will contain the unvisited nodes, initially containing all nodes.
3. Create a distance array dist[] where dist[i] represents the shortest distance from the source node to node i. Initialize dist[] with infinity for all nodes except the source node, which is initialized with 0.
4. While Q is not empty:
   a. Select the node u from Q with the smallest dist[u].
   b. Remove u from Q and add it to S.
   c. For each neighbor v of u:
      i. Calculate the tentative distance new_dist = dist[u] + weight(u, v), where weight(u, v) is the weight of the edge from u to v.
      ii. If new_dist < dist[v], update dist[v] to new_dist.
5. The dist[] array now contains the shortest distances from the source node to all other nodes.

```

**Complexity Analysis:**

1. **Time Complexity:** The time complexity of Dijkstra's Algorithm depends on the data structure used to implement the set of unvisited nodes (Q). Using a min-priority queue (such as a binary heap) yields a time complexity of O(V*log(V) + E), where V is the number of nodes and E is the number of edges in the graph. In the worst case, it is O(V^2) when a simple array is used as a priority queue.

2. **Space Complexity:** The space complexity of the algorithm is O(V), where V is the number of nodes, as it requires storage for the distance array and the sets S and Q.

**Conclusion:**

Dijkstra's Algorithm is a fundamental algorithm for finding the shortest path in a weighted graph. By implementing this algorithm, you can efficiently solve various real-world problems that involve finding optimal routes. Understanding its principles and complexities is essential for any student of algorithms and computer science.

## Files

- [main.c](./main.c)
- [main.min.c](./main.min.c)