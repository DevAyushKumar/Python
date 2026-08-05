'''## 1. How Computer Memory (RAM) Works

* **RAM (Random Access Memory):** Can be visualized as a grid of contiguous storage cells/slots, each associated with a unique numerical **Memory Address** (e.g., address `100`, `101`, `102`).
* **Byte Size:** In standard computer systems, each memory slot or unit holds **1 Byte** ($8\text{ bits}$) of data.
* **Primitive Types & Memory Consumption:**
  * **Char / Byte:** Consumes $1\text{ byte}$ of memory.
  * **Integer (32-bit):** Consumes $4\text{ bytes}$ of memory contiguous in sequence.
  * **Float / Double (64-bit):** Consumes $8\text{ bytes}$ of memory.

---

## 2. Arrays in Memory (Static Arrays)

An **Array** is a contiguous block of allocated memory cells in RAM designed to hold multiple items of the same data type.

### Memory Allocation Mechanics
* When an array of size $N$ integers is instantiated, the operating system reserves a continuous sequence of $N \times 4\text{ bytes}$ in RAM.
* Example: An integer array of size $5$ at starting memory address `1000` occupies memory addresses `1000` through `1019`.

### Direct Memory Address Calculation Formula
Because array elements are stored contiguously, calculating the physical memory address of any element at `index` takes **$O(1)$ constant time**:

$$\text{Address of } A[\text{index}] = \text{Base Address} + (\text{index} \times \text{Size of Data Type})$$

> **Why Arrays are 0-Indexed:** The index represents the **offset** (number of element steps) from the `Base Address`. At index `0`, the offset is `0`, leading directly to the start of the memory block.

---

## 3. Arrays vs. Strings in Memory

* **String:** Under the hood, a string is stored as an array of characters (`char[]`).
* **Character Encoding (ASCII / Unicode):** Each character maps to a specific numerical value stored inside a single byte slot in RAM (e.g., `'A'` maps to integer value `65`).

---

## 4. Static Arrays vs. Dynamic Arrays

| Characteristic | Static Array | Dynamic Array (e.g., Python `list`, C++ `std::vector`, Java `ArrayList`) |
| :--- | :--- | :--- |
| **Size Allocation** | Fixed size defined upon creation; cannot be expanded. | Automatically expands as elements are added. |
| **Capacity vs. Size** | Capacity and length are always identical. | **Size:** Number of items currently stored.<br>**Capacity:** Total slots reserved in RAM. |
| **Resizing Behavior** | Unsupported. | When capacity fills, allocates a new memory block **double the size** ($2\times$) and copies over all existing items. |
| **Insertion Time Complexity** | $O(1)$ if index is known, but size limit is strict. | **Amortized $O(1)$:** Resizing takes $O(n)$ time occasionally, but across $n$ insertions, average cost per append is $O(1)$. |

---

## 5. Summary of Common Array Operations & Time Complexity

* **Access (Read by index):** $O(1)$ constant time — computed instantly via memory offset formula.
* **Search (Find value):** $O(n)$ linear time — requires iterating cell-by-cell.
* **Insertion / Deletion at End:** $O(1)$ amortized time for dynamic arrays.
* **Insertion / Deletion at Start / Middle:** $O(n)$ linear time — requires shifting all remaining elements forward/backward in memory to maintain contiguity.'''