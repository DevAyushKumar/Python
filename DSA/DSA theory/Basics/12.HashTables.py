'''Introduction to Hash Tables and Dictionaries
================================================================================
1. WHAT IS A DICTIONARY (MAP / ASSOCIATIVE ARRAY)?
================================================================================
- Definition: An abstract data structure storing key-value pairs where keys map directly to associated values.
- Core Operations:
  * Search (Lookup): Given a key (e.g., "Paul"), retrieve its value (e.g., 29).
  * Insert (Put): Add a new key-value entry (e.g., "Bob" -> 8).
  * Delete (Remove): Remove an existing key-value entry.
- Goal: Achieve O(1) constant-time performance on average for search, insert, and delete.

================================================================================
2. HASH TABLE ARCHITECTURE & HASH FUNCTIONS
================================================================================
- Underlying Structure: An array of fixed size `m` (called buckets or slots).
- Hash Function: A mathematical function `h(key)` that maps an arbitrary key (e.g., string, object) into a valid array index `[0, m - 1]`.
  * Index Computation: `index = h(key) % m`
- Criteria for a Good Hash Function:
  1. Fast to compute in O(1) time.
  2. Minimizes collisions by distributing keys uniformly across array indices.
  * Example standard algorithm: `djb2` (widely used in hash table implementations).

================================================================================
3. COLLISION RESOLUTION TECHNIQUE 1: SEPARATE CHAINING
================================================================================
- Collision: Occurs when two distinct keys produce the same array index (`h(k1) % m == h(k2) % m`).
- Chaining Mechanism:
  * Each array bucket stores a pointer/reference to a Linked List.
  * All key-value pairs hashing to that bucket are prepended/appended to that linked list.
- Performance & Load Factor (alpha = n / m):
  * `n` = number of stored elements, `m` = array size.
  * Insertion: O(1) time (insert at head of linked list).
  * Search/Delete: O(1 + alpha) average time.
  * If the load factor `alpha` is kept small (e.g., alpha <= 1.0), search/delete operations run in O(1) average time.

================================================================================
4. COLLISION RESOLUTION TECHNIQUE 2: OPEN ADDRESSING
================================================================================
In Open Addressing, all key-value pairs are stored directly inside the array without external linked lists.

--- Method A: Linear Probing ---
- Mechanism: If a collision occurs at index `i`, check the immediate next slot `(i + 1) % m`, then `(i + 2) % m`, until an empty slot is found.
- Drawback: Primary Clustering — consecutive filled slots form large clusters, leading to long probe sequences and degraded performance.

--- Method B: Double Hashing (Preferred Open Addressing Strategy) ---
- Mechanism: Uses two independent hash functions `h1(key)` and `h2(key)` to determine dynamic jump offsets.
  * Initial Probe: `index = h1(key) % m`
  * Subsequent Probes (if collision):
    - 1st retry: `(h1(key) + 1 * c) % m`
    - 2nd retry: `(h1(key) + 2 * c) % m`
    - k-th retry: `(h1(key) + k * c) % m`
    - where `c = (h2(key) % (m - 1)) + 1` (guarantees `c` is in range `[1, m - 1]`).
- Full Coverage Requirement:
  * Greatest Common Divisor `gcd(c, m)` MUST equal 1 so the probing cycle covers every bucket in the table.
  * Best practice: Set table size `m` to a prime number.

================================================================================
5. TIME COMPLEXITY & LOAD FACTOR DYNAMICS
================================================================================
- Double Hashing Probe Bound:
  * Average elements checked during Search/Insert: `1 / (1 - alpha)`
  * Example: If `alpha = 2/3` (table is 66% full), average checks = `1 / (1 - 2/3) = 3` checks.

- Complexity Breakdown:

| Operation | Average Case | Worst Case (All keys collide) |
| :--- | :--- | :--- |
| **Search** | O(1) | O(n) |
| **Insert** | O(1) | O(n) |
| **Delete** | O(1) | O(n) |

- Dynamic Resizing & Rehashing:
  * When `alpha` exceeds a threshold (e.g., `alpha > 2/3` or `alpha > 0.75`), allocate a new array of roughly double size (next prime number).
  * Rehash all existing keys into the new table.
  * Amortized cost per insertion remains O(1).'''