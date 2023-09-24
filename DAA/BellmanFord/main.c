// Bellman Ford Algorithm in C

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

//struct for the edges of the graph
typedef struct Edge {
    int u; //start vertex of the edge
    int v; //end vertex of the edge
    int weight; //weight of the edge (u,v)
} edge_t;

//Graph - it consists of edges
typedef struct Graph {
    int num_vertices; //total number of vertices in the graph
    int num_edges; //total number of edges in the graph
    edge_t* edges; //array of edges
} graph;

void display_int_array(int arr[], int size) {
    for (int i = 0; i < size; i++) 
        printf("%.2d ", arr[i]);
    printf("\n");
}

void display_char_array(int arr[], int size) {
    for (int i = 0; i < size; i++) 
        printf(" %c ", arr[i] + 65);
    printf("\n");
}

void bellmanford(graph* g, int source) {
    //total vertex in the graph g
    int total_vertices = g->num_vertices;
    //total edge in the graph g
    int total_edges = g->num_edges;

    //distance array
    //size equal to the number of vertices of the graph g
    int *distance_array = (int*)malloc(sizeof(int)*total_vertices);

    //predecessor array
    //size equal to the number of vertices of the graph g
    int *predecessor_array = (int*)malloc(sizeof(int)*total_vertices);

    //step 1: fill the distance array and predecessor array
    for (int i = 0; i < total_vertices; i++) {
        distance_array[i] = INT_MAX;
        predecessor_array[i] = 0;
    }

    //mark the source vertex
    distance_array[source] = 0;


    //step 2: relax edges |V| - 1 times
    int u, v, weight;
    for (int i = 1; i <= total_vertices - 1; i++) {
        for (int j = 0; j < total_edges; j++) {
            //get the edge data
            u = g->edges[j].u;
            v = g->edges[j].v;
            weight = g->edges[j].weight;

            if (distance_array[u] != INT_MAX && distance_array[v] > distance_array[u] + weight) {
                distance_array[v] = distance_array[u] + weight;
                predecessor_array[v] = u;
            }
        }
    }

    //step 3: detect negative cycle
    //if value changes then we have a negative cycle in the graph
    //and we cannot find the shortest distances
    for (int i = 0; i < total_edges; i++) {
        u = g->edges[i].u;
        v = g->edges[i].v;
        weight = g->edges[i].weight;
        if (distance_array[u] != INT_MAX && distance_array[v] > distance_array[u] + weight) {
            printf("Negative weight cycle detected!\n");
            return;
        }
    }

    //No negative weight cycle found!
    //print the distance and predecessor array
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

    graph * g = (graph*)malloc(sizeof(graph));
    g->num_vertices = 9;
    g->num_edges = 14;
    g->edges = (edge_t*)malloc(g->num_edges * sizeof(edge_t));


    // (A, B, 4)
    g->edges[0].u = 0;
    g->edges[0].v = 1;
    g->edges[0].weight = 4;
    
    // (A, H, 8)
    g->edges[1].u = 0;
    g->edges[1].v = 7;
    g->edges[1].weight = 8;

    // (B, C, 8)
    g->edges[2].u = 1;
    g->edges[2].v = 2;
    g->edges[2].weight = 8;

    // (B, H, 11)
    g->edges[3].u = 1;
    g->edges[3].v = 7;
    g->edges[3].weight = 11;

    // (C, D, 7)
    g->edges[4].u = 2;
    g->edges[4].v = 3;
    g->edges[4].weight = 7;

    // (C, F, -4)
    g->edges[5].u = 2;
    g->edges[5].v = 5;
    g->edges[5].weight = -4;

    // (C, I, -2)
    g->edges[6].u = 2;
    g->edges[6].v = 8;
    g->edges[6].weight = -2;

    // (D, E, 9)
    g->edges[7].u = 3;
    g->edges[7].v = 4;
    g->edges[7].weight = 9;

    // (D, F, 14)
    g->edges[8].u = 3;
    g->edges[8].v = 5;
    g->edges[8].weight = 14;

    // (E, F, 10)
    g->edges[9].u = 4;
    g->edges[9].v = 5;
    g->edges[9].weight = 10;

    // (F, G, 2)
    g->edges[10].u = 5;
    g->edges[10].v = 6;
    g->edges[10].weight = 2;

    // (G, H, 1)
    g->edges[11].u = 6;
    g->edges[11].v = 7;
    g->edges[11].weight = 1;

    // (G, I, 6)
    g->edges[12].u = 6;
    g->edges[12].v = 8;
    g->edges[12].weight = 6;

    // (H, I, 7)
    g->edges[13].u = 7;
    g->edges[13].v = 8;
    g->edges[13].weight = 7;


    bellmanford(g, 0); //0 is the source vertex

    return 0;
}


