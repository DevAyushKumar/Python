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
    
'''