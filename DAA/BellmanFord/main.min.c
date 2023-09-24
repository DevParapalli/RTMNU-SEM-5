
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Edge {
    int u;
    int v;
    int weight;
} edge_t;

typedef struct Graph {
    int num_vertices;
    int num_edges;
    edge_t* edges;
} graph;

void display_int_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%.2d ", arr[i]);
    }
    printf("\n");
}

void display_char_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf(" %c ", arr[i] + 65);
    }
    printf("\n");
}

void bellmanford(graph* g, int source) {
    int total_vertices = g->num_vertices;
    int total_edges = g->num_edges;

    int* distance_array = (int*)malloc(sizeof(int) * total_vertices);
    int* predecessor_array = (int*)malloc(sizeof(int) * total_vertices);
    for (int i = 0; i < total_vertices; i++) {
        distance_array[i] = INT_MAX;
        predecessor_array[i] = 0;
    }

    distance_array[source] = 0;

    int u, v, weight;
    for (int i = 1; i <= total_vertices - 1; i++) {
        for (int j = 0; j < total_edges; j++) {
            u = g->edges[j].u;
            v = g->edges[j].v;
            weight = g->edges[j].weight;
            if (distance_array[u] != INT_MAX && distance_array[v] > distance_array[u] + weight) {
                distance_array[v] = distance_array[u] + weight;
                predecessor_array[v] = u;
            }
        }
    }

    for (int i = 0; i < total_edges; i++) {
        u = g->edges[i].u;
        v = g->edges[i].v;
        weight = g->edges[i].weight;
        if (distance_array[u] != INT_MAX && distance_array[v] > distance_array[u] + weight) {
            printf("Negative weight cycle detected!\n");
            return;
        }
    }

    printf("Vertices:          ");
    for (int i = 0; i < total_vertices; ++i) {
        printf(" %c ", i + 65);
    }
    printf("\nDistance array:    ");
    display_int_array(distance_array, total_vertices);
    printf("Predecessor array: ");
    display_char_array(predecessor_array, total_vertices);
}

int main(void) {

    graph* g = (graph*)malloc(sizeof(graph));
    g->num_vertices = 9;
    g->num_edges = 14;
    g->edges = (edge_t*)malloc(g->num_edges * sizeof(edge_t));

    g->edges[0].u = 0;
    g->edges[0].v = 1;
    g->edges[0].weight = 4;

    g->edges[1].u = 0;
    g->edges[1].v = 7;
    g->edges[1].weight = 8;

    g->edges[2].u = 1;
    g->edges[2].v = 2;
    g->edges[2].weight = 8;

    g->edges[3].u = 1;
    g->edges[3].v = 7;
    g->edges[3].weight = 11;

    g->edges[4].u = 2;
    g->edges[4].v = 3;
    g->edges[4].weight = 7;

    g->edges[5].u = 2;
    g->edges[5].v = 5;
    g->edges[5].weight = -4;

    g->edges[6].u = 2;
    g->edges[6].v = 8;
    g->edges[6].weight = -2;

    g->edges[7].u = 3;
    g->edges[7].v = 4;
    g->edges[7].weight = 9;

    g->edges[8].u = 3;
    g->edges[8].v = 5;
    g->edges[8].weight = 14;

    g->edges[9].u = 4;
    g->edges[9].v = 5;
    g->edges[9].weight = 10;

    g->edges[10].u = 5;
    g->edges[10].v = 6;
    g->edges[10].weight = 2;

    g->edges[11].u = 6;
    g->edges[11].v = 7;
    g->edges[11].weight = 1;

    g->edges[12].u = 6;
    g->edges[12].v = 8;
    g->edges[12].weight = 6;

    g->edges[13].u = 7;
    g->edges[13].v = 8;
    g->edges[13].weight = 7;

    bellmanford(g, 0);
    return 0;
}
