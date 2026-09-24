"""
Problem: Product of Array Except Self (LeetCode 238)
-----------------------------------------------------
Given an integer array nums, return an array answer such that answer[i] is the
product of all elements of nums except nums[i]. No division allowed.

Approach: Prefix and suffix products
- left[i] = product of elements to the left of i
- right[i] = product of elements to the right of i
- answer[i] = left[i] * right[i]

Time:  O(n)
Space: O(n) output (O(1) extra if we reuse answer)
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    # Left pass: answer[i] = product of nums[0..i-1]
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Right pass: multiply by product of nums[i+1..n-1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([0, 1, 2, 3]) == [0, 0, 0, 0]
    assert product_except_self([2, 3, 4]) == [12, 8, 6]
    assert product_except_self([1]) == [1]
    print("All Product of Array Except Self tests passed.")
