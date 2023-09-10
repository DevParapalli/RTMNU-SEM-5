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

    // algo! start
    qsort(edges, num_edges, sizeof(edge_t), compare_edge);

    set_t * _vertices = createSet();

    for(int i = 0; i < num_edges; i++) {
        setInclude(_vertices, edges[i].from);
        setInclude(_vertices, edges[i].to);
        printf("%c -> %c (%d)\n", *edges[i].from, *edges[i].to, edges[i].weight);
    }

    printf("(Vertices, Edges) -> (%d, %d)\n", _vertices->len, num_edges);

    set_t * set_array[MAX_ARR_SIZE];
    int set_array_len = 0;

    int k_edges[MAX_ARR_SIZE];
    int k_edges_len = 0;

    for(int i = 0; i < num_edges && k_edges_len < _vertices->len - 1; i++) {
        // Iterate Edges

        // find set of from and to
        int _from_set_index = -1;
        int _to_set_index = -1;
        for(int j = 0; j < set_array_len; j++) {
            if(setIncludes(set_array[j], edges[i].from)) _from_set_index = j;
            if(setIncludes(set_array[j], edges[i].to)) _to_set_index = j;
        }

        // if both aren't in a set, create new set, add to list, increment set_array_len
        if (_from_set_index == -1 && _to_set_index == -1) {
            set_array[set_array_len++] = createSet();
            setInclude(set_array[set_array_len-1], edges[i].from);
            setInclude(set_array[set_array_len-1], edges[i].to);
        } 
        // Incase from node is not in a set, add to the set of to node
        else if (_from_set_index == -1) {
            setInclude(set_array[_to_set_index], edges[i].from);
        } 
        // Incase to node is not in a set, add to the set of from node
        else if (_to_set_index == -1) {
            setInclude(set_array[_from_set_index], edges[i].to);
        } 
        // if both are in different sets, merge the sets
        else if (_from_set_index != _to_set_index) {
            for(int j = 0; j < set_array[_to_set_index]->len; j++) {
                setInclude(set_array[_from_set_index], &set_array[_to_set_index]->elements[j]);
            }
            set_array[_to_set_index] = set_array[set_array_len-1];
            set_array_len--;
        } else if (_from_set_index == _to_set_index) {
            // if both are in same set, skip
            continue;
        } else {
            printf("Hope this line never needs to run!\n");
        }

        // Once code reaches here, it means that the edge is to be added to MST

        k_edges[k_edges_len++] = i;
    }

    printf("Kruskal's MST\n");
    int weight = 0;
    for(int i = 0; i < k_edges_len; i++) {
        printf("%c -> %c (%d)\n", *edges[k_edges[i]].from, *edges[k_edges[i]].to, edges[k_edges[i]].weight);
        weight += edges[k_edges[i]].weight;
    }

    printf("Total Weight: %d\n", weight);

}
