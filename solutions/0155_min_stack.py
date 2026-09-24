"""
Problem: Min Stack (LeetCode 155)
----------------------------------
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Approach: Auxiliary stack tracking running minimum
- Main stack stores values.
- Min stack stores the current minimum at each depth.

Time:  O(1) for all operations
Space: O(n)
"""
from typing import Optional


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2
    ms.pop()
    ms.pop()
    assert ms.stack == []
    print("All Min Stack tests passed.")
