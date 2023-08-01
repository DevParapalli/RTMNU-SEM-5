#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r) {
    // Malloc space for copies of 2 arrays
    int * leftArray = (int *)malloc((m - l)*sizeof(int));
    int * rightArray = (int *)malloc((r - (m+1)) * sizeof(int));
    
    // Copy the arrays
    for(int i = 0; i < m - l + 1; i++) {leftArray[i] = arr[l + i];}
    for(int i = 0; i < r - m; i++) {rightArray[i] = arr[m + 1 + i];}
    
    // algo! start:merge
    int lp = 0, rp = 0, ap = l;
    for(; lp < m - l + 1 && rp < r - m;) {
        if (leftArray[lp] <= rightArray[rp]) arr[ap++] = leftArray[lp++];
        else arr[ap++] = rightArray[rp++];
    }
    // Copy the remaining elements
    while (lp < m - l +1) arr[ap++] = leftArray[lp++];
    while (rp < r - m) arr[ap++] = rightArray[rp++];
    // algo! end:merge
}

void merge_sort(int arr[], int l, int r) {
    if ( l < r) {
        int mid = l + (r - l) / 2;
    merge_sort(arr, l, mid);
    merge_sort(arr, mid+1, r);
    merge(arr, l, mid, r);
    }
}

void main() {
    int arr[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    for (int i = 0; i < 10 ; i++) {
        printf("%d\t", arr[i]);
    }
    printf("\n");
    merge_sort(arr, 0 , 9);
    for (int i = 0; i < 10 ; i++) {
        printf("%d\t", arr[i]);
    }

}