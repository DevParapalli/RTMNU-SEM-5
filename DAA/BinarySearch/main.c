#include <stdio.h>
#include <stdlib.h>

#define ARR_SIZE 10
#define MAX_VAL 100
#define RAND_SEED 773

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    srand(RAND_SEED);  // Using srand and seeding with constant to get reproducible results

    int arr[ARR_SIZE];
    for (int i = 0; i < ARR_SIZE; i++) {
        arr[i] = rand() % MAX_VAL;
    }

    qsort(arr, ARR_SIZE, sizeof(int), cmp);

    printf("Sorted array:   ");
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("%.2d ", arr[i]);
    }

    int low = 0, high = ARR_SIZE - 1, mid, element;

    printf("\nEnter the element to be searched: ");
    scanf("%d", &element);

    // algo! start
    while(low <= high) {
        mid = (low + high) / 2;
        if (arr[mid] == element) {
            printf("Element found at index %d\n", mid);
            return 0;
        } else if (arr[mid] < element) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    // algo! end
}