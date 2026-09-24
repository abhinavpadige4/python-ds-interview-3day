"""
Problem: Linked List Cycle (LeetCode 141)
------------------------------------------
Given the head of a linked list, determine if it contains a cycle.

Approach: Floyd's Tortoise and Hare
- Slow pointer moves 1 step, fast pointer moves 2 steps.
- If there's a cycle, they must meet.

Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def has_cycle_set(head: Optional[ListNode]) -> bool:
    """Alternative: hash set. O(n) time, O(n) space."""
    seen = set()
    cur = head
    while cur:
        if id(cur) in seen:
            return True
        seen.add(id(cur))
        cur = cur.next
    return False


def _build_with_cycle(vals, cycle_pos=None):
    """Build a list; if cycle_pos is not None, tail points to index cycle_pos."""
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos is not None:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    assert has_cycle(_build_with_cycle([3, 2, 0, -4], 1)) is True
    assert has_cycle(_build_with_cycle([1, 2], 0)) is True
    assert has_cycle(_build_with_cycle([1])) is False
    assert has_cycle(_build_with_cycle([])) is False
    assert has_cycle_set(_build_with_cycle([1, 2, 3, 4], 2)) is True
    print("All Linked List Cycle tests passed.")
