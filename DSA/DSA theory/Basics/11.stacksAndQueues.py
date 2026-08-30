'''# Comprehensive Notes: Introduction to Stacks, Queues, and Deques (Data Structures & Algorithms #12)

Source: CS Dojo (Instructor: YK)
Video Link: https://www.youtube.com/watch?v=A3ZUpyrnCbM

================================================================================
1. STACK DATA STRUCTURE
================================================================================
- Mental Model: A stack of pancakes on a plate. You can only place a pancake on top or eat/remove the topmost pancake.
- Principle: LIFO (Last-In, First-Out)
  * The last element added to the stack is the first one removed.
  * Access to elements in the middle or bottom is restricted.

- Core Operations:
  * Push (Add): Insert an element at the top of the stack -> O(1) time.
  * Pop (Delete/Remove): Remove and return the element at the top of the stack -> O(1) time.
  * Peek/Top: View the top element without removing it -> O(1) time.

- Array-Based Implementation:
  * Maintain a single pointer/index `top_pointer` initialized to -1 (indicating empty stack).
  * Push: Increment `top_pointer` by 1 and insert the value at `arr[top_pointer]`.
  * Pop: Decrement `top_pointer` by 1 (no need to erase the old cell memory).

================================================================================
2. QUEUE DATA STRUCTURE
================================================================================
- Mental Model: A line of people waiting for a service. People join the back of the line and leave from the front.
- Principle: FIFO (First-In, First-Out)
  * The first element inserted is the first one processed and removed.

- Core Operations:
  * Enqueue (Add): Insert an element at the rear/back of the queue -> O(1) time.
  * Dequeue (Remove): Remove the element from the front/head of the queue -> O(1) time.

- Circular Array-Based Implementation:
  * Uses two pointers:
    - `front`: Points directly to the first valid element.
    - `rear` (or `next_available`): Points to the index right after the last element.
  * Queue Empty Condition: `front == rear`.
  * Wrapping Around: When pointers reach the end of the array (index `n`), they wrap around to index 0 using the modulo operator: `pointer = (pointer + 1) % capacity`.
  * Maximum Capacity: In this design, an array of size `n` stores up to `n - 1` elements to distinguish an empty queue from a full queue.

================================================================================
3. DEQUE (DOUBLE-ENDED QUEUE)
================================================================================
- Definition: A generalized, flexible queue where insertions and deletions can occur at BOTH ends (front/left and back/right).

- Core Operations:
  * `add_front` (or `push_left`): Insert element at the beginning -> O(1) time.
  * `add_rear` (or `push_right` / `enqueue`): Insert element at the end -> O(1) time.
  * `remove_front` (or `pop_left` / `dequeue`): Remove element from the beginning -> O(1) time.
  * `remove_rear` (or `pop_right`): Remove element from the end -> O(1) time.

- Implementation: Typically built using a Circular Buffer/Array or a Doubly Linked List.

================================================================================
4. TIME AND SPACE COMPLEXITY MATRIX
================================================================================
- Stack Operations (Array/List based):
  * Push: O(1) Time | O(1) Auxiliary Space
  * Pop:  O(1) Time | O(1) Auxiliary Space
  * Peek: O(1) Time | O(1) Auxiliary Space

- Queue Operations (Circular Array based):
  * Enqueue: O(1) Time | O(1) Auxiliary Space
  * Dequeue: O(1) Time | O(1) Auxiliary Space

- Deque Operations:
  * Insert Front/Rear: O(1) Time | O(1) Auxiliary Space
  * Delete Front/Rear: O(1) Time | O(1) Auxiliary Space

================================================================================
5. CLASSIC INTERVIEW APPLICATION: BALANCED BRACKETS PROBLEM
================================================================================
- Problem: Given a string containing brackets '()', '[]', and '{}', determine if the bracket sequence is valid/balanced.

- Rules:
  1. Open brackets must be closed by the same type of closing bracket.
  2. Open brackets must be closed in the correct order (e.g., "{[()]}" is valid, "[(])" is invalid).

- Stack Algorithm Solution:
  * Initialize an empty Stack.
  * Iterate through each character in the string:
    - If character is an opening bracket ('(', '[', '{'), push it onto the stack.
    - If character is a closing bracket (')', ']', '}'):
      * If stack is empty -> return False (closing without opening).
      * Pop top element from stack and check if it matches the current closing bracket type. If mismatch -> return False.
  * After scanning the string, return `len(stack) == 0` (True if all opened brackets were closed).

- Complexity:
  * Time Complexity: O(n), where n is the length of the string.
  * Space Complexity: O(n) auxiliary space for the stack in the worst case.'''