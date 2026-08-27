'''# Comprehensive Notes: Introduction to Big O Notation and Time Complexity (Data Structures & Algorithms #7)

================================================================================
1. WHY WE NEED BIG O NOTATION
================================================================================
- Hardware Independence: Actual execution time measured in seconds/milliseconds fluctuates depending on CPU speed, hardware architecture, background tasks, and programming language choice.
- Input-Scale Focus: Evaluates how an algorithm's execution time scales purely as a function of the input size (n).
- Big O Definition: A mathematical notation used to classify algorithms according to how their runtime or space requirements grow as the input size (n) approaches infinity (asymptotic upper bound).

================================================================================
2. DERIVING BIG O: MATHEMATICAL RULES
================================================================================
When determining the Big O time complexity of a function with respect to input size n:

Rule 1: Drop Lower-Order Terms
- As n grows exceedingly large, lower-order terms become insignificant compared to the dominant term.
- Example: If total operations = n^2 + 5n + 100, the n^2 term dominates as n -> infinity. The complexity is O(n^2).

Rule 2: Drop Constant Multipliers
- Constant scaling factors do not change the fundamental growth rate category.
- Example: 5n -> O(n), 100n^2 -> O(n^2), and c * O(1) -> O(1).

================================================================================
3. CODE EXAMPLES & LINE-BY-LINE COMPLEXITY
================================================================================

--- EXAMPLE 1: Summing a 1D Array -> O(n) Linear Time ---

Python Code:
def find_sum(arr):
    total = 0               # Constant time: c1
    for num in arr:         # Loops n times
        total += num        # Constant time inside loop: c2
    return total            # Constant time: c3

Derivation:
- Initialization (total = 0) runs once: takes constant time c1.
- Loop body executes n times: each iteration takes constant time c2, giving total time c2 * n.
- Returning result executes once: takes constant time c3.
- Total Time Function: T(n) = c2 * n + (c1 + c3) = a * n + b
- Dropping constant b and multiplier a yields O(n) Linear Time Complexity.


--- EXAMPLE 2: Accessing Array Element / Fixed Calculations -> O(1) Constant Time ---

Python Code:
def get_first_item(arr):
    if len(arr) > 0:
        return arr[0]       # Instant lookup by offset
    return None

Derivation:
- The operation executes a fixed, constant number of CPU instructions regardless of whether the array contains 5 elements or 5,000,000 elements.
- Total Time Function: T(n) = c
- Yields O(1) Constant Time Complexity.


--- EXAMPLE 3: Summing a 2D Matrix (Nested Loops) -> O(n^2) Quadratic Time ---

Python Code:
def find_sum_2d(matrix):
    total = 0                       # Constant time: c1
    for row in matrix:              # Outer loop runs n times
        for val in row:             # Inner loop runs n times for each row
            total += val            # Executes n * n = n^2 times (cost c2)
    return total                    # Constant time: c3

Derivation:
- For an n x n 2D grid/matrix, the outer loop executes n times.
- For each outer iteration, the inner loop executes n times.
- Total executions of inner statement: n * n = n^2.
- Total Time Function: T(n) = c2 * n^2 + (c1 + c3)
- Dropping lower-order terms and constants yields O(n^2) Quadratic Time Complexity.


--- EXAMPLE 4: Multiple Independent Loops vs. Multiple Variables ---

Case A: Sequential Independent Loops (Add Complexities)
def example_sequential(arr):
    for x in arr:
        print(x)    # Takes O(n)
    
    for y in arr:
        print(y)    # Takes O(n)
Total operations: O(n) + O(n) = O(2n) -> O(n)

Case B: Distinct Inputs (a and b)
def example_two_inputs(arr_a, arr_b):
    for x in arr_a:         # Runs 'a' times
        for y in arr_b:     # Runs 'b' times
            print(x, y)
Because 'a' and 'b' are independent inputs with different lengths, you cannot simplify this to O(n^2).
Correct Big O Complexity: O(a * b) or O(n * m).

================================================================================
4. GROWTH RATES HIERARCHY (FASTEST TO SLOWEST)
================================================================================
1. O(1) - Constant Time: Runtime is invariant to input size (e.g., hash map lookup, array index access).
2. O(log n) - Logarithmic Time: Problem size is halved at each step (e.g., Binary Search).
3. O(n) - Linear Time: Runtime grows in direct 1:1 proportion to input size (e.g., single-pass array traversals).
4. O(n log n) - Linearithmic Time: Optimal comparison-based sorting performance (e.g., Merge Sort, Heap Sort).
5. O(n^2) - Quadratic Time: Nested iterations over the same dataset (e.g., Bubble Sort, 2D matrix scans).
6. O(2^n) - Exponential Time: Operations double with each additional input unit (e.g., naive recursive Fibonacci).
7. O(n!) - Factorial Time: Explores all permutations of a set (e.g., Traveling Salesperson brute force).

================================================================================
5. SPACE COMPLEXITY FUNDAMENTALS
================================================================================
- Definition: The amount of additional working memory (RAM) an algorithm allocates relative to input size n.
- Auxiliary Space: Strict measure of temporary memory created during algorithm execution (excludes input data size).

'''