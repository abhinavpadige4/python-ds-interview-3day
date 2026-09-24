"""
Problem: Maximum Depth of Binary Tree (LeetCode 104)
------------------------------------------------------
Given the root of a binary tree, return its maximum depth.

Approach: Recursion (DFS)
- Depth of a node = 1 + max(depth of left, depth of right).

Time:  O(n)
Space: O(h) where h is tree height (O(log n) balanced, O(n) skewed)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_iterative(root: Optional[TreeNode]) -> int:
    """BFS-based iterative approach."""
    if not root:
        return 0
    from collections import deque
    q = deque([(root, 1)])
    depth = 0
    while q:
        node, d = q.popleft()
        depth = max(depth, d)
        if node.left:
            q.append((node.left, d + 1))
        if node.right:
            q.append((node.right, d + 1))
    return depth


def _build(vals):
    from collections import deque
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    assert max_depth(_build([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(_build([1, None, 2])) == 2
    assert max_depth(None) == 0
    assert max_depth_iterative(_build([1, 2, 3, 4, 5])) == 3
    print("All Maximum Depth of Binary Tree tests passed.")
