#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_VAL 65535


// Number of vertices in the graph
#define V 9

// A function to print the solution matrix
void print_solution(int dist[][V]) {
    printf("The following matrix shows the shortest distances"
           " between every pair of vertices \n");
    for (int i = -1; i < V; i++) {
        printf("%7c", i + 65);
    }
    printf("\n");
    for (int i = 0; i < V; i++) {
        printf("%7c", i + 65);
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == MAX_VAL) {
                printf("%7s", "MAX_VAL");
            } else {
                printf("%7d", dist[i][j]);
            }
        }
        printf("\n");
    }
}

// Solves the all-pairs shortest path
// problem using Floyd Warshall algorithm
void floyd_warshall(int dist[][V]) {
    int j, k, i;

    /* Add all vertices one by one to
	the set of intermediate vertices.
	---> Before start of an iteration, we
	have shortest distances between all
	pairs of vertices such that the shortest
	distances consider only the
	vertices in set {0, 1, 2, .. k-1} as
	intermediate vertices.
	----> After the end of an iteration,
	vertex no. k is added to the set of
	intermediate vertices and the set
	becomes {0, 1, 2, .. k} */
    for (i = 0; i < V; i++) {
        // Pick all vertices as source one by one
        for (j = 0; j < V; j++) {
            // Pick all vertices as destination for the
            // above picked source
            for (k = 0; k < V; k++) {
                // If vertex k is on the shortest path from
                // i to j, then update the value of
                // dist[i][j]
                if (dist[j][i] + dist[i][k] < dist[j][k]) {
                    dist[j][k] = dist[j][i] + dist[i][k];
                }
            }
        }
    }

    // Print the shortest distance matrix
    print_solution(dist);
}

/* A utility function to print solution */

// driver's code
int main() {
    int graph[V][V] =
    {   
        {MAX_VAL,       4, MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL,       8, MAX_VAL},
        {      4, MAX_VAL,       8, MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL,      11, MAX_VAL},
        {MAX_VAL,       8, MAX_VAL,       7, MAX_VAL,       4, MAX_VAL, MAX_VAL,       2},
        {MAX_VAL, MAX_VAL,       7, MAX_VAL,       9,      14, MAX_VAL, MAX_VAL, MAX_VAL},
        {MAX_VAL, MAX_VAL, MAX_VAL,       9, MAX_VAL,      10, MAX_VAL, MAX_VAL, MAX_VAL},
        {MAX_VAL, MAX_VAL,       4,      14,      10, MAX_VAL,       2, MAX_VAL, MAX_VAL},
        {MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL,       2, MAX_VAL,       1,       6},
        {      8,      11, MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL,       1, MAX_VAL,       7},
        {MAX_VAL, MAX_VAL,       2, MAX_VAL, MAX_VAL, MAX_VAL,       6,       7, MAX_VAL}
    };

    // Function call
    floyd_warshall(graph);
    return 0;
}
