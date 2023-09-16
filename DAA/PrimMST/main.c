#include <stdio.h>
#include <stdlib.h>

#define MAX_ARR_SIZE 30

typedef struct Edge {
    char * from;
    char * to;
    int weight;
} edge_t;

typedef struct Set {
    char * elements;
    int len;
} set_t;

set_t * createSet() {
    set_t * set = malloc(sizeof(set_t));
    set->elements = malloc(sizeof(char) * MAX_ARR_SIZE);
    set->len = 0;
    for(int i = 0; i < MAX_ARR_SIZE; i++) set->elements[i] = 0;
    return set;
}

int _setIndex(set_t * set, char * e) {
    if (set->len == 0) return -1;
    for(int i = 0; i < set->len; i++) 
        if(set->elements[i] == *e) 
            return i;
    return -1;
}

int setIncludes(set_t * set, char * e) {
    if (_setIndex(set, e) == -1) return 0; 
    return 1;
}


int setInclude(set_t * set, char * e) {
    if(set->len == MAX_ARR_SIZE) return -2;
    if(setIncludes(set, e)) return -1;
    set->elements[set->len++] = *e;
    return 0;
}

int setExclude(set_t * set, char * e) {
    int _ie = _setIndex(set, e);
    char _t = set->elements[_ie];
    for(int i = _ie; i < set->len - 1; i++) set->elements[i] = set->elements[i+1];
    set->len--;
    return _t;
}

void setDisplay(set_t * set) {
    printf("{");
    for(int i = 0; i < set->len - 1; i++) 
        printf("%c, ", set->elements[i]);
    printf("%c}\n", set->elements[set->len-1]);
}

int compare_edge(const void * a, const void * b){
    return (((edge_t *)a)->weight - ((edge_t *)b)->weight);
}


int main() {
    edge_t edges[] = {
        {"A", "B", 4},
        {"B", "C", 8},
        {"C", "D", 7},
        {"D", "E", 9},
        {"E", "F", 10},
        {"F", "G", 2},
        {"G", "H", 1},
        {"H", "A", 8},
        {"B", "H", 11},
        {"C", "I", 2},
        {"C", "F", 4},
        {"D", "F", 14},
        {"G", "I", 6},
        {"H", "I", 7},
    };

    int num_edges = sizeof(edges)/sizeof(edge_t);

    
    qsort(edges, num_edges, sizeof(edge_t), compare_edge);

    set_t * _vertices = createSet();

    for(int i = 0; i < num_edges; i++) {
        setInclude(_vertices, edges[i].from);
        setInclude(_vertices, edges[i].to);
        printf("%c -> %c (%d)\n", *edges[i].from, *edges[i].to, edges[i].weight);
    }

    printf("(Vertices, Edges) -> (%d, %d)\n", _vertices->len, num_edges);

    set_t * visited = createSet();

    int p_edges[MAX_ARR_SIZE];
    int p_edges_len = 0;

    // algo! start

    // Select the vertex where the minimum edge weight is connected.
    setInclude(visited, edges[0].from); 

    while(visited->len != _vertices->len) {
        for(int i = 0; i < num_edges; i++) {
            if(setIncludes(visited, edges[i].from) && !setIncludes(visited, edges[i].to)) {
                setInclude(visited, edges[i].to);
                p_edges[p_edges_len++] = i;
                break;
            } else if(setIncludes(visited, edges[i].to) && !setIncludes(visited, edges[i].from)) {
                setInclude(visited, edges[i].from);
                p_edges[p_edges_len++] = i;
                break;
            }
        }
    }

    // algo! stop

    printf("Prim's MST\n");
    int weight = 0;
    for(int i = 0; i < p_edges_len; i++) {
        printf("%c -> %c (%d)\n", *edges[p_edges[i]].from, *edges[p_edges[i]].to, edges[p_edges[i]].weight);
        weight += edges[p_edges[i]].weight;
    }

    printf("Total Weight: %d\n", weight);

}
