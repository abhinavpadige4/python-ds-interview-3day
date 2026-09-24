"""
Problem: Top K Frequent Elements (LeetCode 347)
------------------------------------------------
Given an integer array nums and an integer k, return the k most frequent elements.

Approach: Counter + heap (nlargest)
- Count frequencies, then use heapq.nlargest to get top k.

Time:  O(n + k log n)
Space: O(n)
"""
import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]


def top_k_frequent_bucket(nums: List[int], k: int) -> List[int]:
    """Bucket sort approach: O(n) time, O(n) space."""
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    result = []
    for freq in range(len(buckets) - 1, -1, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert top_k_frequent_bucket([4, 1, 1, 4, 6, 3, 3], 2) == [4, 1]
    print("All Top K Frequent Elements tests passed.")
