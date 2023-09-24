Title: Implementation of Floyd-Warshall Algorithm

Introduction:
The Floyd-Warshall algorithm is a dynamic programming technique used to find the shortest path between all pairs of vertices in a weighted graph. It is a versatile algorithm that works with both positive and negative edge weights, provided there are no negative cycles. This practical aims to implement the Floyd-Warshall algorithm in standard compliant C, understand its working principle, and analyze its time and space complexities.

Algorithm Overview:
The Floyd-Warshall algorithm is based on the principle of relaxation, where it iteratively updates the shortest path distances between all pairs of vertices by considering a path through an intermediate vertex. The algorithm initializes a matrix to represent the shortest distances and then iterates through all vertices, considering each vertex as a potential intermediate vertex. During each iteration, it checks if the path through the intermediate vertex yields a shorter distance than the current best-known path. If it does, the distance is updated.

Pseudocode:
```
procedure FloydWarshall(graph G):
    n = number of vertices in G
    dist[][] = initialize a 2D array with distances between vertices

    for k from 1 to n:
        for i from 1 to n:
            for j from 1 to n:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print the final dist[][] matrix
```

Complexity Analysis:
1. Time Complexity:
   - The algorithm has three nested loops, each iterating through all vertices (n).
   - Therefore, the time complexity of the Floyd-Warshall algorithm is O(n^3).
   - It is important to note that the algorithm's time complexity is independent of the graph's density, making it suitable for dense graphs.

2. Space Complexity:
   - The algorithm requires a 2D matrix of size n x n to store the shortest distances.
   - Thus, the space complexity is O(n^2) due to the storage of the dist[][] matrix.


Conclusion:
The Floyd-Warshall algorithm is a powerful tool for finding shortest path distances between all pairs of vertices in a graph. Its time complexity of O(n^3) makes it suitable for various applications, especially when negative edge weights are allowed. By implementing the algorithm in standard compliant C, students can gain a deeper understanding of its working principles and complexities.