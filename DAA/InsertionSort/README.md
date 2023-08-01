# InsertionSort

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is an in-place comparison-based algorithm that works by dividing the input array into two parts: the sorted subarray and the unsorted subarray.

The algorithm iterates over the unsorted subarray, and for each element, it finds the correct position in the sorted subarray by comparing it with each element from right to left until it finds the correct position. It then shifts all the larger elements one position to the right and inserts the element in its correct position.

The best case scenario for Insertion Sort is when the input array is already sorted, in which case the inner loop will never execute, and the time complexity will be O(n). The worst case scenario is when the input array is sorted in reverse order, in which case the inner loop will execute n*(n-1)/2 times, and the time complexity will be O(n^2). The average time complexity of the algorithm is also O(n^2).
