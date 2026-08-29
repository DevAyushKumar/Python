'''# Comprehensive Notes: Introduction to Binary Search (Data Structures & Algorithms #10)

Source: CS Dojo (Instructor: YK)
Video Link: https://www.youtube.com/watch?v=6ysjqCUv3K4

================================================================================
1. PROBLEM STATEMENT & MOTIVATION
================================================================================
- Problem: Given a SORTED array of integers and a target integer, find the index of the target in the array. If the target does not exist, return -1.

- Comparison: Linear Search vs. Binary Search
  * Linear Search:
    - Scans elements sequentially from index 0 until the target is found or a larger element is reached.
    - On average, checks about n/2 elements.
    - Time Complexity: O(n).
  * Binary Search:
    - Prerequisite: The array MUST be sorted.
    - Repeatedly divides the search range in half by checking the middle element.
    - Time Complexity: O(log n).

================================================================================
2. HOW BINARY SEARCH WORKS (STEP-BY-STEP ALGORITHM)
================================================================================
1. Initialize two pointers:
   - left (L) = 0 (pointing to the first element).
   - right (R) = len(arr) - 1 (pointing to the last element).

2. Loop while left <= right:
   - Calculate the middle index:
     mid = (left + right) // 2
   - Compare arr[mid] with target:
     * Case 1: arr[mid] == target
       -> Target found! Return mid.
     * Case 2: arr[mid] > target (Target is smaller)
       -> Target must be in the left half. Narrow search by moving right pointer:
          right = mid - 1
     * Case 3: arr[mid] < target (Target is larger)
       -> Target must be in the right half. Narrow search by moving left pointer:
          left = mid + 1

3. If the loop finishes without finding the target (left > right, search window empty):
   - Return -1.

================================================================================
3. CODE IMPLEMENTATIONS
================================================================================

--- Python Implementation ---

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

# Example Usage:
# arr = [-50, -20, 0, 5, 7, 10, 11, 20, 30, 50]
# print(binary_search(arr, 11))  # Output: 6
# print(binary_search(arr, 12))  # Output: -1


--- Java Implementation ---

public class BinarySearch {
    public static int search(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2; // Prevents potential integer overflow
            
            if (arr[mid] == target) {
                return mid;
            } else if (target < arr[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return -1;
    }
}

================================================================================
4. TIME & SPACE COMPLEXITY ANALYSIS
================================================================================
- Time Complexity: O(log n)
  * Derivation:
    - At step 0: Search range is n elements.
    - At step 1: Search range is n / 2.
    - At step 2: Search range is n / (2^2).
    - At step k: Search range is n / (2^k) ≈ 1.
    - Solving 2^k = n yields k = log2(n) steps.
  * Real-world Scale Example:
    - For an array of 10,000,000 (10 million) elements:
      log2(10,000,000) ≈ 24 comparisons maximum (vs. up to 10,000,000 with linear search).

- Space Complexity: O(1)
  * Iterative Binary Search only uses a few integer pointer variables (left, right, mid), requiring constant auxiliary memory.

================================================================================
5. EXTENSION: SHIFTED / ROTATED SORTED ARRAY SEARCH
================================================================================
- Problem: An array originally sorted is shifted/rotated around an unknown pivot point (e.g., [4, 5, 6, 7, 0, 1, 2]).
- Key Insight: Even in a shifted array, at least one half (left or right) of the array divided by mid is always normally sorted.
- Target check: Identify the sorted half, determine if target lies in that range, and prune the other half in O(log n) time.'''