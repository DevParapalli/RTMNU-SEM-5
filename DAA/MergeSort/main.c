#include <stdio.h>
#include <stdlib.h>

#define ARR_SIZE 10
#define MAX_VAL 100
#define RAND_SEED 773

void merge(int arr[], int l, int m, int r) {
    // Malloc space for copies of 2 arrays
    int *leftArray = (int *)malloc((m - l) * sizeof(int));
    int *rightArray = (int *)malloc((r - (m + 1)) * sizeof(int));

    // Copy the arrays
    for (int i = 0; i < m - l + 1; i++) {
        leftArray[i] = arr[l + i];
    }
    for (int i = 0; i < r - m; i++) {
        rightArray[i] = arr[m + 1 + i];
    }

    // algo! start:merge
    int lp = 0, rp = 0, ap = l;
    for (; lp < m - l + 1 && rp < r - m;) {
        if (leftArray[lp] <= rightArray[rp])
            arr[ap++] = leftArray[lp++];
        else
            arr[ap++] = rightArray[rp++];
    }
    // Copy the remaining elements
    while (lp < m - l + 1) arr[ap++] = leftArray[lp++];
    while (rp < r - m) arr[ap++] = rightArray[rp++];
    // algo! end:merge
}

void merge_sort(int arr[], int l, int r) {
    if (l < r) {
        int mid = l + (r - l) / 2;
        merge_sort(arr, l, mid);
        merge_sort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }
}

void main() {
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

    merge_sort(arr, 0, 9);

    printf("Sorted array:   ");
    for (int i = 0; i < ARR_SIZE; i++) {
        printf("%.2d ", arr[i]);
    }
    printf("\n");
}