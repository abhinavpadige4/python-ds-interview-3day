"""
Problem: Kth Largest Element in an Array (LeetCode 215)
---------------------------------------------------------
Given an integer array nums and an integer k, return the kth largest element.

Approach 1: Min-heap of size k
- Push each element; if heap size > k, pop the smallest.
- The top of the heap is the kth largest.

Time:  O(n log k)
Space: O(k)
"""
import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def find_kth_largest_sort(nums: List[int], k: int) -> int:
    """Alternative: sort. O(n log n) time, O(n) space."""
    return sorted(nums, reverse=True)[k - 1]


def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """Quickselect: average O(n) time, O(1) space."""
    import random
    target = len(nums) - k

    def partition(left, right, pivot_idx):
        pivot_val = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        store = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    def select(left, right):
        if left == right:
            return nums[left]
        pivot_idx = random.randint(left, right)
        pivot_idx = partition(left, right, pivot_idx)
        if pivot_idx == target:
            return nums[pivot_idx]
        elif pivot_idx < target:
            return select(pivot_idx + 1, right)
        else:
            return select(left, pivot_idx - 1)

    return select(0, len(nums) - 1)


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest_sort([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest_quickselect([3, 2, 1, 5, 6, 4], 2) == 5
    print("All Kth Largest Element tests passed.")
