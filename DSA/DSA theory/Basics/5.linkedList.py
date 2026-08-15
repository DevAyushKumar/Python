'''## 1. Core Concepts & Overview

* **Linked List:** A linear data structure composed of distinct elements called **Nodes**, where each node contains data and a pointer/reference to the subsequent node in sequence.
* **Non-Contiguous Memory:** Unlike Arrays, elements in a linked list are **not stored contiguously** in RAM. Each node can be anywhere in memory, tied together solely by reference pointers.
* **Head:** A reference pointing to the very first node of the linked list. If `head == null` (or `None`), the list is completely empty.
* **Tail:** The final node in the list. Its `next` reference points to `null` (or `None`), marking the end of the sequence.

---

## 2. Anatomy of a Node

A Node object contains two essential components:
1. **`data` (or `val`):** The actual value or payload stored inside the node (e.g., Integer, String, custom Object).
2. **`next`:** A reference variable storing the memory address of the next `Node` object in the chain.

1. Linked List Architecture
Linked List: A linear data structure composed of distinct elements called Nodes, where each node holds data and a pointer/reference to the next node.

Non-Contiguous Allocation: Nodes can be scattered across different locations in RAM, linked solely via reference pointers.

Head: Reference pointing to the first node. If head == null, the list is empty.

Tail: The final node whose next reference points to null (or None).

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Data: 4     │     │  Data: 2     │     │  Data: 10    │
│  Next: ───┼─┼────>│  Next: ───┼─┼────>│  Next: null  │
└──────────────┘     └──────────────┘     └──────────────┘
  (Head Node)                               (Tail Node)
  
2. Node Implementation & Counting Traversal
Java Implementation
Java
public class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedListUtils {
    // Traverse and count nodes: Time O(n), Space O(1)
    public static int countNodes(Node head) {
        int count = 0;
        Node current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }
}

Python Implementation
Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count
    
# Data Structures: Time & Space Complexity Cheat Sheet

---

## 1. Time Complexity Breakdown

### Static Array
* **Access (Index):** O(1) — Direct computation via memory address offset.
* **Search (Value):** O(n) — Linear traversal required.
* **Search (Sorted):** O(log n) — Using Binary Search.
* **Insertion (Head):** O(n) — Must shift all elements one position to the right.
* **Insertion (Tail):** O(1) — Instant if unused capacity exists.
* **Insertion (Middle):** O(n) — Traversal + shifting remaining elements.
* **Deletion (Head):** O(n) — Must shift all elements one position to the left.
* **Deletion (Tail):** O(1) — Instant index boundary decrement.
* **Deletion (Middle):** O(n) — Shifting remaining elements to fill the gap.

### Dynamic Array (`ArrayList`, `std::vector`, Python `list`)
* **Access (Index):** O(1) — Direct address offset calculation.
* **Search (Value):** O(n) — Linear scan.
* **Search (Sorted):** O(log n) — Binary Search.
* **Insertion (Head):** O(n) — Shift all items right.
* **Insertion (Tail):** O(1) Amortized — O(n) only during array resizing / capacity doubling.
* **Insertion (Middle):** O(n) — Shift elements right.
* **Deletion (Head):** O(n) — Shift elements left.
* **Deletion (Tail):** O(1) — Simple boundary update.
* **Deletion (Middle):** O(n) — Shift elements left.

### Singly Linked List
* **Access (Index):** O(n) — Must traverse node-by-node from the head.
* **Search (Value):** O(n) — Must follow `next` pointers sequentially.
* **Search (Sorted):** O(n) — Binary Search not possible without random access.
* **Insertion (Head):** O(1) — Update new node's `next` pointer to head, reassign head.
* **Insertion (Tail):** O(1) with tail pointer / O(n) without tail pointer.
* **Insertion (Middle):** O(n) to find position, then O(1) pointer adjustment.
* **Deletion (Head):** O(1) — Move head reference to `head.next`.
* **Deletion (Tail):** O(n) — Must traverse to the second-to-last node to clear `next`.
* **Deletion (Middle):** O(n) to find node, then O(1) pointer redirection.

### Doubly Linked List
* **Access (Index):** O(n) — Can traverse from head or tail depending on index proximity.
* **Search (Value):** O(n) — Sequential pointer traversal.
* **Search (Sorted):** O(n) — Linear scan only.
* **Insertion (Head):** O(1) — Direct update of `head` and `prev`/`next` links.
* **Insertion (Tail):** O(1) — Direct update using `tail` pointer.
* **Insertion (Middle):** O(n) to find position / O(1) if target node reference is already provided.
* **Deletion (Head):** O(1) — Instant pointer reassignments.
* **Deletion (Tail):** O(1) — Instant pointer update via `prev` reference on tail.
* **Deletion (Middle):** O(n) to locate node / O(1) given direct reference to that node.

---

## 2. Summary Comparison Matrix

| Operation | Static Array | Dynamic Array | Singly Linked List | Doubly Linked List |
| :--- | :--- | :--- | :--- | :--- |
| **Access (Index)** | O(1) | O(1) | O(n) | O(n) |
| **Search (Value)** | O(n) | O(n) | O(n) | O(n) |
| **Search (Sorted)** | O(log n) | O(log n) | O(n) | O(n) |
| **Insert at Head** | O(n) | O(n) | O(1) | O(1) |
| **Insert at Tail** | O(1) | O(1) Amortized | O(1) *(with tail)* | O(1) |
| **Insert at Middle**| O(n) | O(n) | O(n) | O(n) |
| **Delete at Head** | O(n) | O(n) | O(1) | O(1) |
| **Delete at Tail** | O(1) | O(1) | O(n) | O(1) |
| **Delete at Middle**| O(n) | O(n) | O(n) | O(n) |

---

## 3. Memory & Hardware Architecture Trade-offs

* **Auxiliary Memory per Element:**
  * Arrays (Static & Dynamic): 0 bytes overhead.
  * Singly Linked List: 4 to 8 bytes per node (for the `next` pointer reference).
  * Doubly Linked List: 8 to 16 bytes per node (for both `prev` and `next` pointer references).
* **Memory Allocation:**
  * Arrays: Stored in contiguous blocks of RAM.
  * Linked Lists: Dynamically allocated across scattered memory addresses.
* **CPU Cache Locality:**
  * Arrays: **High spatial locality** — contiguous memory fits in CPU L1/L2 cache lines for fast iterations.
  * Linked Lists: **Poor cache locality** — non-contiguous memory leads to frequent CPU cache misses during pointer chasing.'''