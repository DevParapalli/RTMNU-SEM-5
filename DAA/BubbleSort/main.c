#include <stdio.h>
#include <stdlib.h>

#define SWAP(x, y) do { int temp = x; x = y; y = temp; } while (0)

#define ARR_SIZE 10
#define MAX_VAL 100
#define RAND_SEED 773

int main() {
    srand(RAND_SEED); // Using srand and seeding with constant to get reproducible results

    int arr[ARR_SIZE];
    for (int i = 0; i < ARR_SIZE; i++) {
        arr[i] = rand() % MAX_VAL;
    }

    printf("Unsorted array: ");
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("%.2d ", arr[i]);
    }
    printf("\n");
    // algo! start
    for(int i = 0; i < ARR_SIZE; i++) {
        for(int j = 0; j < ARR_SIZE - i - 1; j++) {
            if(arr[j] > arr[j + 1]) {
                SWAP(arr[j], arr[j + 1]);
            }
        }
    }
    // algo! end
    printf("Sorted array:   ");
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("%.2d ", arr[i]);
    }
}