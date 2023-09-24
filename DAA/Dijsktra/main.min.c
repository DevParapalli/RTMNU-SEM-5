#include <limits.h>
#include <stdbool.h>
#include <stdio.h>

int minDistance(int dist[], bool sptSet[]) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < 9; v++) 
        if (sptSet[v] == false && dist[v] <= min) 
            min = dist[v], min_index = v;
    return min_index;
}

void printSolution(int dist[]) {
    printf("Vertex \t\t Distance from Source\n");
    for (int i = 0; i < 9; i++) printf("%d \t\t\t\t %d\n", i, dist[i]);
}

void dijkstra(int graph[9][9], int src) {
    int dist[9];
    bool sptSet[9];
    for (int i = 0; i < 9; i++) {
        dist[i] = INT_MAX, sptSet[i] = false;
    }
    dist[src] = 0;
    for (int count = 0; count < 9 - 1; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = true;
        for (int v = 0; v < 9; v++) 
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) 
                dist[v] = dist[u] + graph[u][v];
    }
    printSolution(dist);
}

int main() {
    int graph[9][9] = {
        {0,  4, 0,  0,  0, 0, 0,  8, 0},  
        {4,  0, 8,  0,  0, 0, 0, 11, 0}, 
        {0,  8, 0,  7,  0, 4, 0,  0, 2},
        {0,  0, 7,  0,  9, 14, 0, 0, 0},  
        {0,  0, 0,  0,  0,  2, 0, 1, 6},  
        {0,  0, 0,  9,  0, 10, 0, 0, 0}, 
        {0,  0, 4, 14, 10,  0, 2, 0, 0},
        {8, 11, 0,  0,  0,  0, 1, 0, 7}, 
        {0,  0, 2,  0,  0,  0, 6, 7, 0}
        };

    dijkstra(graph, 0);

    return 0;
}
