# Add Two Numbers (Linked List Representation)

## Problem Statement

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

---

## Example 1:

### Input:
`l1 = [2, 4, 3], l2 = [5, 6, 4]`

### Process:
- **Number represented by l1**: 342 (reverse of [2, 4, 3])
- **Number represented by l2**: 465 (reverse of [5, 6, 4])
- **Sum**: 342 + 465 = **807**

### Output:
`[7, 0, 8]`

---

## Diagram:

### Given Linked Lists:
```
l1: 2 -> 4 -> 3
l2: 5 -> 6 -> 4
```

### Output Linked List:
```
Result: 7 -> 0 -> 8
```

---

## Explanation:

- Each node contains a single digit.
- The two linked lists represent numbers in reverse order.
- Perform digit-by-digit addition, accounting for any carry value.

---

## Constraints:

1. The linked lists are **non-empty**.
2. The digits are stored in reverse order.
3. Each node contains a **single digit**.

---

## Implementation Steps:

1. Traverse both linked lists simultaneously.
2. At each node, sum the values of the current nodes (and carry if present).
3. If the sum exceeds `9`, carry over the extra value to the next node.
4. Continue until all nodes in both linked lists are processed.
5. Return the resulting linked list.