"""
Problem: Two Sum (LeetCode 1)
--------------------------------
Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to `target`.

Assume exactly one solution exists; the same element cannot be used twice.

Approach: Hash Map (one pass)
- For each number, compute complement = target - num.
- If complement is already in the map, we found the pair.
- Otherwise, store num -> index in the map.

Time:  O(n)
Space: O(n)
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # unreachable given problem constraints


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    print("All Two Sum tests passed.")
