#include <stdio.h>
#include <stdlib.h>

struct HuffmanNode {
    char data;
    long int freq;
    struct HuffmanNode *left;
    struct HuffmanNode *right;
};

struct MinHeap {
    long int size;
    long int capacity;
    struct HuffmanNode **array;
};

struct HuffmanNode *newNode(char data, long int freq) {
    struct HuffmanNode *temp = (struct HuffmanNode *)malloc(sizeof(struct HuffmanNode));
    temp->left = temp->right = NULL;
    temp->data = data;
    temp->freq = freq;
    return temp;
}

struct MinHeap *createMinHeap(long int capacity) {
    struct MinHeap *minHeap = (struct MinHeap *)malloc(sizeof(struct MinHeap));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->array = (struct HuffmanNode **)malloc(minHeap->capacity * sizeof(struct HuffmanNode *));
    return minHeap;
}




