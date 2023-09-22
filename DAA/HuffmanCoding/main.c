#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#define MAX_ARR_SIZE 100
#define MAX_STR_SIZE 1000

typedef struct huffman_node {
    char data;
    long int freq;
    struct huffman_node *left;
    struct huffman_node *right;
    char *code;
} node_t;

node_t *create_huffman_node(char data, long int freq) {
    node_t *temp = (node_t *)malloc(sizeof(node_t));
    temp->left = temp->right = NULL;
    temp->data = data;
    temp->freq = freq;
    return temp;
}

int compare_node_alphabetically(const void * a, const void * b) {
    node_t *node_a = (node_t *)a;
    node_t *node_b = (node_t *)b;
    return (node_a->data - node_b->data);
}


int get_character_index(node_t array[], char character, int size) {
    for(int i = 0; i < size; i++) {
        if(array[i].data == character) {
            return i;
        }
    }
    return -1;
}

void heapify_nodes(node_t * array, int size, int index) {
    int smallest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < size && array[left].freq < array[smallest].freq) {
        smallest = left;
    }

    if (right < size && array[right].freq < array[smallest].freq) {
        smallest = right;
    }

    if (smallest != index) {
        node_t temp = array[index];
        array[index] = array[smallest];
        array[smallest] = temp;
        heapify_nodes(array, size, smallest);
    }
}

void add_node_to_heap(node_t * array, int size, node_t node) {
    array[size] = node;
    int i = size;
    while (i != 0 && array[(i - 1) / 2].freq > array[i].freq) {
        node_t temp = array[i];
        array[i] = array[(i - 1) / 2];
        array[(i - 1) / 2] = temp;
        i = (i - 1) / 2;
    }
}

node_t remove_node_from_heap(node_t * array, int size) {
    node_t min = array[0];
    array[0] = array[size - 1];
    heapify_nodes(array, size - 1, 0);
    return min;
}

void build_huffman_heap(node_t * array, int size) {
    for(int i = size / 2 - 1; i >= 0; i--) {
        heapify_nodes(array, size, i);
    }
}

void generate_huffman_codes(node_t * array, int *array_size, node_t * root, char * code) {
    if ((root->left == NULL) && (root->right == NULL)) {
        // Leaf Node, contains data
        root->code = code;
        array[(*array_size)++] = *root;
        return;
    }
    
    char * left_code = (char *)malloc(strlen(code) + 1);
    strcpy(left_code, code);
    strcat(left_code, "0");
    generate_huffman_codes(array, array_size, root->left, left_code);
    
    char * right_code = (char *)malloc(strlen(code) + 1);
    strcpy(right_code, code);
    strcat(right_code, "1");
    generate_huffman_codes(array, array_size, root->right, right_code);
}

int main(int argc, char *argv[]) {
    node_t array_of_nodes[MAX_ARR_SIZE];
    int array_of_nodes_size = 0;
    char *input;
    input = (char *)malloc(MAX_STR_SIZE * sizeof(char));
    
    printf("Enter the string: ");
    scanf("%[^\n]s", input);   
    int length_of_input = strlen(input);
    // Creating a frequency table
    for(int i = 0; i < length_of_input; i++) {
        int nodeIndex = get_character_index(array_of_nodes, input[i], array_of_nodes_size);
        if (nodeIndex == -1) {
            array_of_nodes[array_of_nodes_size] = *create_huffman_node(input[i], 1);
            array_of_nodes_size++;
        } else {
            array_of_nodes[nodeIndex].freq++;
        }
    }

    build_huffman_heap(array_of_nodes, array_of_nodes_size);

    while (array_of_nodes_size > 1) {
        node_t *left = (node_t *)malloc(sizeof(node_t));
        node_t *right = (node_t *)malloc(sizeof(node_t));
        *left = remove_node_from_heap(array_of_nodes, array_of_nodes_size);
        array_of_nodes_size--;
        *right = remove_node_from_heap(array_of_nodes, array_of_nodes_size);
        array_of_nodes_size--;
        node_t *parent = create_huffman_node('\0', left->freq + right->freq);
        parent->left = left;
        parent->right = right;
        add_node_to_heap(array_of_nodes, array_of_nodes_size, *parent);
        array_of_nodes_size++;
    }


    node_t root = remove_node_from_heap(array_of_nodes, array_of_nodes_size);
    array_of_nodes_size--;

    generate_huffman_codes(array_of_nodes, &array_of_nodes_size, &root, "");

    qsort(array_of_nodes, array_of_nodes_size, sizeof(node_t), compare_node_alphabetically);
    printf("Codes:\n");
    for(int i = 0; i < array_of_nodes_size; i++) {
        printf("%c\t%s\n", array_of_nodes[i].data, array_of_nodes[i].code);
    }

    printf("Original String:\n");
    for(int i = 0; i < length_of_input; i++) {
        char a = input[i];
        for (int j = 0; j < 8; j++) {
            printf("%d", !!((a << j) & 0x80));
        }
    }
    printf("\nLength:%ld\n", strlen(input) * 8);


    printf("Compressed String:\n");
    char * encoded_string = (char *)malloc(MAX_STR_SIZE * sizeof(char));
    encoded_string[0] = '\0';

    for(int i = 0; i < length_of_input; i++) {
        int nodeIndex = get_character_index(array_of_nodes, input[i], array_of_nodes_size);
        strcat(encoded_string, array_of_nodes[nodeIndex].code);
    }
    printf("%s\nLength:%ld\n", encoded_string, strlen(encoded_string));
    printf("Space Saved: %ld\n", (length_of_input * 8) - strlen(encoded_string));
}
