#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_VAL 65535

#define V 9

void print_solution(int dist[][V]) {
    printf("Solution Matrix:\n");
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

void floyd_warshall(int dist[][V]) {
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            for (int k = 0; k < V; k++) {
                if (dist[j][i] + dist[i][k] < dist[j][k]) {
                    dist[j][k] = dist[j][i] + dist[i][k];
                }
            }
        }
    }
    print_solution(dist);
}

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

    floyd_warshall(graph);
    return 0;
}
