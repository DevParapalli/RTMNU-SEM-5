# Selection Sort

Selection sort is a simple and intuitive sorting algorithm that works by repeatedly finding the smallest element from an unsorted array and moving it to the beginning. The process is then repeated with the remaining elements until the entire array is sorted.

The time complexity of selection sort is O(n^2), where n is the number of elements in the array. The best case scenario is when the array is already sorted, which takes O(n^2) time because it still has to compare each element with the rest of the elements in the array. The worst case scenario is when the array is sorted in reverse order, which also takes O(n^2) time because it requires maximum swaps to place the elements in their correct position. Therefore, selection sort is not a very efficient sorting algorithm for large arrays, but it can be useful for small arrays or for sorting partially sorted arrays.

## Files

- [main.c](./main.c)
