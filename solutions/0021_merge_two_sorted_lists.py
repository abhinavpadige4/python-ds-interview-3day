"""
Problem: Merge Two Sorted Lists (LeetCode 21)
-----------------------------------------------
Given two sorted linked lists, merge them into one sorted list by splicing nodes.

Approach: Dummy head + two pointers
- Use a dummy node to avoid edge cases with the head.
- At each step, attach the smaller node and advance that pointer.

Time:  O(n + m)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


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
    assert _to_list(merge_two_lists(_build([1, 2, 4]), _build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert _to_list(merge_two_lists(None, _build([1]))) == [1]
    assert _to_list(merge_two_lists(_build([1]), None)) == [1]
    assert _to_list(merge_two_lists(None, None)) == []
    print("All Merge Two Sorted Lists tests passed.")
