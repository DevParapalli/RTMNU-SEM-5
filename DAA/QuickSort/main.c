#include <stdio.h>
#include <stdlib.h>

#define SWAP(x, y) do { int temp = x; x = y; y = temp; } while (0)

#define ARR_SIZE 10
#define MAX_VAL 100
#define RAND_SEED 773

int partition(int arr[], int lo, int hi) {
    int pivot = arr[(lo + hi)/2];
    int i = lo - 1;
    int j = hi + 1;

    while(1) {
        do {
            i++;
        } while(arr[i] < pivot);

        do {
            j--;
        } while(arr[j] > pivot);

        if(i >= j) {
            return j;
        }

        SWAP(arr[i], arr[j]);
    }
}

void quickSort(int *arr, int lo, int hi) {
    if (lo >= 0 && hi >= 0 && lo < hi) {
        int p = partition(arr, lo, hi);
        quickSort(arr, lo, p); // Pivot included in left half
        quickSort(arr, p + 1, hi);
    }
}

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
    // algo! start
    quickSort(arr, 0, ARR_SIZE - 1);
    // algo! end
    printf("Sorted array:   ");
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("%.2d ", arr[i]);
    }
    printf("\n");
}