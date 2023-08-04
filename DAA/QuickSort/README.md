# QuickSort

QuickSort is a widely used sorting algorithm known for its efficiency and effectiveness in sorting large datasets. It follows the divide-and-conquer paradigm and was developed by Tony Hoare in 1960. The algorithm works by recursively partitioning the input array into smaller sub-arrays and then sorting them. It is an in-place sorting algorithm, meaning it sorts the elements directly within the original array without using additional memory.

Here's a step-by-step explanation of the QuickSort algorithm: 
1. **Choose a Pivot** : The first step is to choose a pivot element from the array. The pivot is a value that serves as a reference point for partitioning the array. 
2. **Partitioning** : Rearrange the elements in the array such that all elements less than the pivot are placed before the pivot, and all elements greater than the pivot are placed after it. The pivot is now in its final sorted position. 
3. **Recursion** : After partitioning, the array is divided into two sub-arrays. Recursively apply QuickSort to both sub-arrays created in the previous step. 
4. **Base Case** : The recursion stops when the sub-arrays become small enough (e.g., one or two elements) to be considered sorted trivially. This is the base case of the recursion. 
5. **Combine** : Since the elements are sorted in place during the partitioning step, no additional work is needed to combine the sorted sub-arrays.

```pseudocode
// Sorts a (portion of an) array, divides it into partitions, then sorts those
algorithm quicksort(A, lo, hi) is 
  if lo >= 0 && hi >= 0 && lo < hi then
    p := partition(A, lo, hi) 
    quicksort(A, lo, p) // Note: the pivot is now included
    quicksort(A, p + 1, hi) 

// Divides array into two partitions
algorithm partition(A, lo, hi) is 
  // Pivot value
  pivot := A[ floor((hi - lo)/2) + lo ] // The value in the middle of the array

  // Left index
  i := lo - 1 

  // Right index
  j := hi + 1

  loop forever 
    // Move the left index to the right at least once and while the element at
    // the left index is less than the pivot
    do i := i + 1 while A[i] < pivot
    
    // Move the right index to the left at least once and while the element at
    // the right index is greater than the pivot
    do j := j - 1 while A[j] > pivot

    // If the indices crossed, return
    if i >= j then return j
    
    // Swap the elements at the left and right indices
    swap A[i] with A[j]
```

QuickSort has an average and best-case time complexity of O(n log n), where 'n' is the number of elements in the array. However, in the worst-case scenario (when the pivot is the smallest or largest element in the array), the time complexity can degrade to O(n^2). Nevertheless, the worst-case scenario is quite rare, and in practice, QuickSort outperforms many other sorting algorithms.

