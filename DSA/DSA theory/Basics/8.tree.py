'''Introduction to Trees (Data Structures & Algorithms #9)
================================================================================
1. WHAT IS A TREE DATA STRUCTURE?
================================================================================
- Linked List vs. Tree:
  * In a Linked List, each node links to only ONE subsequent node (single linear direction).
  * In a Tree, each node can link to MULTIPLE child nodes (hierarchical branching structure).
  * A Linked List is technically a degenerate tree where each node has at most 1 child.

- Essential Components of a Tree:
  * Node: An individual entity containing data/value and references/pointers to its children.
  * Root Node: The topmost entry node of the tree. It has NO parent node (no other node points to it).
  * Leaf Node: A node with no children (all child references point to null/None).
  * Reachability: There must be a direct path from the root node to every other node in the tree structure.

================================================================================
2. RULES: WHAT QUALIFIES AS A VALID TREE?
================================================================================
To be a valid tree data structure, the structure MUST satisfy the following constraints:

1. Single Inward Reference Rule:
   - Exactly ONE parent reference can point to any node (except the root, which has 0).
   - If two different nodes point to the SAME child node, it is NOT a tree (it is a Directed Acyclic Graph or general graph).

2. Acyclic Rule (No Cycles / Loops):
   - A tree CANNOT contain cycles. If following links can lead you back in a circle, it is NOT a tree.

================================================================================
3. BINARY TREES & NODE REPRESENTATIONS
================================================================================
- General Tree Node: Can have N child pointers (e.g., child1, child2, child3 or a list/array of children).
- Binary Tree: A specialized tree where each node has AT MOST two children, typically named "left" and "right".

--- Node Class Definition in Java ---

public class Node {
    int data;
    Node left;
    Node right;

    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

--- Node Class Definition in Python ---

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

================================================================================
4. ALGORITHM: FIND SUM OF ALL NODES IN A BINARY TREE
================================================================================
Problem: Given the root of a binary tree, calculate and return the sum of all node values in O(n) time.

--- Recursive Solution Strategy ---
1. Base Case:
   - If root is null/None (empty tree/leaf child), return 0.
2. Recursive Step:
   - Sum = root.data + find_sum(root.left) + find_sum(root.right)

--- Python Code ---

def find_sum(root):
    # Base Case: Empty subtree has a sum of 0
    if root is None:
        return 0
    
    # Recursive Case: Current node value + Left Subtree Sum + Right Subtree Sum
    return root.data + find_sum(root.left) + find_sum(root.right)

--- Java Code ---

public class BinaryTree {
    public static int findSum(Node root) {
        // Base Case: Empty subtree
        if (root == null) {
            return 0;
        }
        
        // Recursive Case
        return root.data + findSum(root.left) + findSum(root.right);
    }
}

================================================================================
5. COMPLEXITY ANALYSIS
================================================================================
- Time Complexity: O(n)
  * Total recursive calls made: For a tree with n nodes, the function is invoked once per node plus once for each null child (at most 2n + 1 total calls).
  * Work per call: Checking base condition and adding numbers takes constant time O(1).
  * Total Time: O(1) * O(n) = O(n), where n is the number of nodes.

- Space Complexity (Call Stack):
  * Balanced Binary Tree: O(log n) auxiliary stack space (height of the tree).
  * Skewed Binary Tree (Worst Case): O(n) auxiliary stack space (tree degenerates into a linked list).'''