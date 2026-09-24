# Python Data Structures Interview Prep — 3-Day Plan

A focused 3-day plan to prepare for a Python data structures interview. Each day covers a topic cluster with solved practice problems, complexity analysis, and interview talking points.

## 3-Day Schedule

### Day 1 — Built-in Structures: Lists, Dicts, Sets, Tuples
Focus: time/space complexity of built-ins, hash-map patterns, two-pointer, sliding window.

| # | Problem | File |
|---|---------|------|
| 1 | Two Sum | `solutions/0001_two_sum.py` |
| 2 | Valid Anagram | `solutions/0012_valid_anagram.py` |
| 3 | Group Anagrams | `solutions/0049_group_anagrams.py` |
| 4 | Contains Duplicate | `solutions/0024_contains_duplicate.py` |
| 5 | Top K Frequent Elements | `solutions/0034_top_k_frequent_elements.py` |
| 6 | Product of Array Except Self | `solutions/00238_product_of_array_except_self.py` |
| 7 | Longest Substring Without Repeating Characters | `solutions/0003_longest_substring_without_repeating.py` |

### Day 2 — Linked Lists, Stacks, Queues
Focus: pointer manipulation, iterative vs recursive, monotonic stacks, BFS/DFS with explicit stacks.

| # | Problem | File |
|---|---------|------|
| 8 | Reverse Linked List | `solutions/0021_reverse_linked_list.py` |
| 9 | Detect Cycle in Linked List | `solutions/00141_linked_list_cycle.py` |
| 10 | Merge Two Sorted Lists | `solutions/0021_merge_two_sorted_lists.py` |
| 11 | Valid Parentheses | `solutions/0020_valid_parentheses.py` |
| 12 | Min Stack | `solutions/00155_min_stack.py` |
| 13 | Daily Temperatures | `solutions/00739_daily_temperatures.py` |
| 14 | Implement Queue using Stacks | `solutions/00232_implement_queue_using_stacks.py` |

### Day 3 — Trees, Heaps, Graphs
Focus: recursion on trees, heap-based top-K, BFS/DFS on graphs, topological sort.

| # | Problem | File |
|---|---------|------|
| 15 | Binary Tree Level Order Traversal | `solutions/00102_binary_tree_level_order.py` |
| 16 | Maximum Depth of Binary Tree | `solutions/00104_max_depth_binary_tree.py` |
| 17 | Validate Binary Search Tree | `solutions/0098_validate_bst.py` |
| 18 | Kth Largest Element in Array | `solutions/00215_kth_largest_element.py` |
| 19 | Number of Islands | `solutions/00200_number_of_islands.py` |
| 20 | Course Schedule (Topological Sort) | `solutions/00207_course_schedule.py` |
| 21 | Clone Graph | `solutions/00133_clone_graph.py` |

## Complexity Cheat Sheet

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| `list` | O(1) | O(n) | O(1) amortized | O(n) |
| `dict` | O(1) avg | O(1) avg | O(1) avg | O(1) avg |
| `set` | — | O(1) avg | O(1) avg | O(1) avg |
| `tuple` | O(1) | O(n) | immutable | immutable |
| `deque` | O(1) | O(n) | O(1) both ends | O(1) both ends |
| `heap` (heapq) | O(1) min | O(n) | O(log n) | O(log n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| BST | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg |
| Graph (adj list) | — | O(V+E) | O(1) | O(1) |

## How to Use This Repo

1. Read the day's topic notes in this README.
2. Open each solution file — every file contains a full working implementation with:
   - Problem statement
   - Approach explanation
   - Time & space complexity
   - Edge cases
   - A `if __name__ == "__main__":` block with sample tests
3. Run any file directly: `python solutions/0001_two_sum.py`
4. Re-implement from scratch before looking at the solution.

## Interview Talking Points

- **Hash maps**: O(1) average, O(n) worst case (collisions). Python's `dict` preserves insertion order (3.7+).
- **Sets**: use for O(1) membership; `set` is unordered, `frozenset` is hashable.
- **Two-pointer**: sorted arrays, in-place swaps, sliding window.
- **Linked lists**: dummy head simplifies edge cases; Floyd's tortoise-and-hare for cycles.
- **Stacks**: LIFO; monotonic stacks for "next greater element" style problems.
- **Queues**: FIFO; `collections.deque` for O(1) popleft (list.pop(0) is O(n)).
- **Trees**: recursion is natural; BFS with `deque` for level order; BST invariant: left < node < right.
- **Heaps**: `heapq` is a min-heap; negate values for max-heap; top-K problems.
- **Graphs**: adjacency list; DFS for reachability, BFS for shortest path in unweighted; Kahn's algorithm for topological sort.
