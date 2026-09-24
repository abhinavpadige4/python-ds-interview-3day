"""
Problem: Implement Queue using Stacks (LeetCode 232)
------------------------------------------------------
Implement a FIFO queue using two stacks.

Approach: Two stacks with lazy transfer
- in_stack: receives pushes.
- out_stack: receives pops; refill from in_stack when empty.
- Amortized O(1) per operation.

Time:  O(1) amortized per op
Space: O(n)
"""


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer(self) -> None:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        if not self.out_stack:
            self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.empty() is True
    q.push(3)
    q.push(4)
    q.push(5)
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5
    assert q.empty() is True
    print("All Implement Queue using Stacks tests passed.")
