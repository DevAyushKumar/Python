'''# Comprehensive Notes: A Complete Overview of Quicksort (Data Structures & Algorithms #11)

Source: CS Dojo (Instructor: YK)
Video Link: https://www.youtube.com/watch?v=0SkOjNaO1XY

================================================================================
1. OVERVIEW & DIVIDE-AND-CONQUER STRATEGY
================================================================================
- Quicksort: An efficient, in-place, comparison-based, divide-and-conquer sorting algorithm.
- Core Mechanism:
  1. Base Case: If the subarray has 0 or 1 element (left >= right), it is already sorted. Return immediately.
  2. Partitioning (The Key Step):
     - Select an element as the "pivot" (e.g., the last element arr[right]).
     - Rearrange elements such that:
       * All elements smaller than the pivot move to the left of the pivot.
       * All elements greater than or equal to the pivot move to the right of the pivot.
     - Place the pivot into its final sorted position and return its index `p`.
  3. Recursive Step:
     - Recursively apply quicksort to the left subarray: `qs(arr, left, p - 1)`.
     - Recursively apply quicksort to the right subarray: `qs(arr, p + 1, right)`.

================================================================================
2. LOMUTO PARTITION SCHEME (STEP-BY-STEP)
================================================================================
- Pointers used during partition:
  * `pivot`: Value at `arr[right]`.
  * `i`: Tracks the boundary of elements strictly smaller than the pivot (initialized to `left - 1`).
  * `j`: Scans from `left` up to `right - 1`.

- Partition Invariants:
  * Elements from `left` to `i` are `< pivot`.
  * Elements from `i + 1` to `j - 1` are `>= pivot`.

- Procedure:
  1. For `j = left` to `right - 1`:
     - If `arr[j] < pivot`:
       * Increment `i` by 1 (`i++`).
       * Swap `arr[i]` with `arr[j]`.
  2. After loop terminates, place pivot in correct position:
     - Swap `arr[i + 1]` with `arr[right]` (the pivot).
  3. Return new pivot index `i + 1`.

================================================================================
3. CODE IMPLEMENTATIONS
================================================================================

--- Python Implementation ---

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Place pivot in its final position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quicksort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quicksort(arr, left, p - 1)   # Sort left partition
        quicksort(arr, p + 1, right)  # Sort right partition

# Helper wrapper function
def sort(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr

# Example Usage:
# data = [3, 2, -1, 4, 0, -2, 5]
# print(sort(data))  # Output: [-2, -1, 0, 2, 3, 4, 5]


--- Java Implementation ---

public class QuickSort {
    public static int partition(int[] arr, int left, int right) {
        int pivot = arr[right];
        int i = left - 1;
        
        for (int j = left; j < right; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        // Swap pivot into correct position
        int temp = arr[i + 1];
        arr[i + 1] = arr[right];
        arr[right] = temp;
        
        return i + 1;
    }
    
    public static void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int p = partition(arr, left, right);
            quickSort(arr, left, p - 1);
            quickSort(arr, p + 1, right);
        }
    }
}

================================================================================
4. TIME & SPACE COMPLEXITY ANALYSIS
================================================================================
- Best-Case Time Complexity: O(n log n)
  * Occurs when the pivot is always close to the median, splitting the array into two roughly equal halves of size ~n/2.
  * Tree depth: log2(n) levels.
  * Work per level: O(n) partition time.
  * Total: O(n) * O(log n) = O(n log n).

- Average-Case Time Complexity: O(n log n)
  * Occurs under random permutations with distinct keys.

- Worst-Case Time Complexity: O(n^2)
  * Occurs when the array is already sorted (ascending or descending) or contains all identical elements.
  * Pivot creates an extreme imbalance: 0 elements on one side, n - 1 on the other.
  * Total operations: (n - 1) + (n - 2) + ... + 1 = n(n - 1)/2 = O(n^2).

- Space Complexity:
  * In-place data sorting (no secondary arrays allocated).
  * Best/Average Call Stack Space: O(log n).
  * Worst-Case Call Stack Space: O(n).

================================================================================
5. PRACTICAL OPTIMIZATIONS & ADVANCED TECHNIQUES
================================================================================
1. Randomized Pivot Selection:
   - Pick a random index between `left` and `right`, swap it with `arr[right]`, then partition.
   - Prevents O(n^2) worst-case performance on pre-sorted data.

2. Median-of-Three Pivot:
   - Sample 3 elements (first, middle, last), find their median, and use it as the pivot.
   - Significantly reduces the probability of hitting worst-case unbalanced splits.

3. Three-Way Quicksort (Dutch National Flag Partitioning):
   - Divides the array into 3 partitions: `< pivot`, `== pivot`, and `> pivot`.
   - Handles arrays with heavy duplicate elements in O(n) linear time instead of degrading to O(n^2).'''