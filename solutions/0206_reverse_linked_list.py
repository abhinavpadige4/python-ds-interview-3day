"""
Problem: Reverse Linked List (LeetCode 206)
--------------------------------------------
Given the head of a singly linked list, reverse the list and return the new head.

Approach: Iterative pointer reversal
- Use three pointers: prev, curr, next_node.
- For each node, redirect curr.next to prev, then advance.

Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """Recursive approach: O(n) time, O(n) stack space."""
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def _build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert _to_list(reverse_list(_build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert _to_list(reverse_list(_build([1, 2]))) == [2, 1]
    assert _to_list(reverse_list(_build([1]))) == [1]
    assert _to_list(reverse_list(None)) == []
    assert _to_list(reverse_list_recursive(_build([1, 2, 3]))) == [3, 2, 1]
    print("All Reverse Linked List tests passed.")
