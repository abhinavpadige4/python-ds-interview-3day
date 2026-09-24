"""
Problem: Contains Duplicate (LeetCode 217)
-------------------------------------------
Given an integer array nums, return True if any value appears at least twice.

Approach: Set
- Insert each element into a set; if insertion finds a duplicate, return True.

Time:  O(n)
Space: O(n)
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


def contains_duplicate_sort(nums: List[int]) -> bool:
    """Alternative: sort then compare adjacent. O(n log n) time, O(1) space."""
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate([]) is False
    assert contains_duplicate_sort([3, 1, 2, 3]) is True
    print("All Contains Duplicate tests passed.")
