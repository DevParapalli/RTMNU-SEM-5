#include <stdio.h>
#include <stdlib.h>

#define MAX(x, y) ((x) > (y) ? (x) : (y))

#define ARR_SIZE 5
#define KNAPSACK_CAPACITY 30
#define MAX_VAL 100
#define RAND_SEED 773

typedef struct Item {
    int value;
    int weight;
} item;

int compare_item(const void *a, const void *b) {
    return ((item *)b)->value / ((item *)b)->weight - ((item *)a)->value / ((item *)a)->weight;
}

int contains(int *arr, int size, int element) {
    for (int i = 0; i < size; i++) if (arr[i] == element) return 1;
    return 0;
}

int knapsack(int capacity, item *items) {
    int _cap = capacity;
        for (int i = 0; i < ARR_SIZE; i++) {
            if (items[i].weight <= capacity) {
                capacity -= items[i].weight;
            }
        }
    return _cap - capacity;
}

int main(int argc, char **argv) {
    srand(RAND_SEED);

    item items[ARR_SIZE];
    for (int i = 0; i < ARR_SIZE; i++) {
        items[i].value = rand() % MAX_VAL;
        items[i].weight = rand() % MAX_VAL;
    }
    int n = sizeof(items) / sizeof(items[0]);
    qsort(items, n, sizeof(item), compare_item);

    printf("Items:\n");
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("Item %.2d: value: %.2d, weight: %.2d\n", i, items[i].value, items[i].weight);
    }
    printf("Capacity: %d\n", KNAPSACK_CAPACITY);
    printf("Maximum Value Possible using Greedy Strategy: %d\n", knapsack(KNAPSACK_CAPACITY, items));
    return 0;
}