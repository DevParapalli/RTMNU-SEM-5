#include <stdio.h>
#include <stdlib.h>

#define ARR_SIZE 10
#define MAX_VAL 100
#define RAND_SEED 773

int main() {
    srand(RAND_SEED);  // Using srand and seeding with constant to get reproducible results

    int arr[ARR_SIZE];
    for (int i = 0; i < ARR_SIZE; i++) {
        arr[i] = rand() % MAX_VAL;
    }

    printf("Unsorted array: ");
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("%.2d ", arr[i]);
    }
    printf("\n");
    printf("Enter the element to be searched: ");
    int idx = -1, element;
    scanf("%d", &element);
    // algo! start
    for (int i = 0; i < ARR_SIZE; i++) {
        if (arr[i] == element) {
            idx = i;
            break;
        }
    }
    // algo! end
    if (idx == -1) {
        printf("Element not found\n");
    } else {
        printf("Element found at index %d\n", idx);
    }
}