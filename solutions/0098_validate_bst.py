"""
Problem: Validate Binary Search Tree (LeetCode 98)
----------------------------------------------------
Given the root of a binary tree, determine if it is a valid BST.

A valid BST satisfies:
- Left subtree contains only values < node.val
- Right subtree contains only values > node.val
- Both subtrees are also valid BSTs

Approach: Recursion with bounds
- Pass (low, high) bounds down; each node must be within bounds.

Time:  O(n)
Space: O(h)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def validate(node, low=float("-inf"), high=float("inf")):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root)


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
    assert is_valid_bst(_build([2, 1, 3])) is True
    assert is_valid_bst(_build([5, 1, 4, None, None, 3, 6])) is False
    assert is_valid_bst(_build([1])) is True
    assert is_valid_bst(None) is True
    print("All Validate BST tests passed.")
