# MergeSort

Merge Sort is a popular comparison-based sorting algorithm that follows the divide-and-conquer strategy to sort an array or a list. It breaks the input array into smaller subarrays, recursively sorts them, and then merges the sorted subarrays to produce the final sorted array. The key steps in the Merge Sort algorithm are as follows:

1. **Divide** : The input array is divided into two equal or nearly equal halves.
2. **Conquer** : The two halves are sorted recursively using the Merge Sort algorithm.
3. **Merge** : The sorted halves are merged to produce the final sorted array.

Here's a high-level explanation of the Merge Sort algorithm:

1. If the input array has zero or one element, it is already considered sorted.
2. Otherwise, split the array into two halves, and recursively call Merge Sort on each half.
3. Merge the sorted halves using a helper function called "Merge."

## Time Complexity Analysis

The time complexity of Merge Sort is determined by the number of comparisons and the number of merges that take place during the sorting process.

1. **Divide** : This step doesn't involve any comparisons and simply requires calculating the mid-point of the array. It can be done in constant time, O(1).
2. **Conquer** : The array is divided into two halves, and each half is sorted recursively. The time complexity for the conquer step is calculated based on the number of recursive calls. The array is divided into two halves at each recursive call, so the total number of recursive calls is log₂(n), where n is the size of the input array.
3. **Merge** : The merge step involves comparing elements from two sorted arrays and merging them into a single sorted array. The number of comparisons required to merge two sorted arrays of size m and n is O(m + n).

Combining these steps, the time complexity of Merge Sort can be expressed as:

`T(n) = 2 * T(n/2) + O(n)`

where:

- `T(n)` is the time taken to sort an array of size n.

Using the Master theorem, we can solve the recurrence relation and find the time complexity of Merge Sort:

- `T(n)` = O(n log n)

Thus, the time complexity of Merge Sort is O(n log n).

**Note** : Merge Sort has an average, best, and worst-case time complexity of O(n log n). Additionally, it has a space complexity of O(n) due to the need for auxiliary space during the merge step to merge the sorted arrays.
