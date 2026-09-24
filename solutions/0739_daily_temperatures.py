"""
Problem: Daily Temperatures (LeetCode 739)
--------------------------------------------
Given an array of integers temperatures, return an array answer where answer[i]
is the number of days you have to wait until a warmer temperature.

Approach: Monotonic stack
- Stack holds indices of temperatures not yet matched.
- For each new warmer temp, pop all cooler indices and record the gap.

Time:  O(n)
Space: O(n)
"""
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []  # indices with pending warmer day
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 5, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    assert daily_temperatures([1]) == [0]
    print("All Daily Temperatures tests passed.")
