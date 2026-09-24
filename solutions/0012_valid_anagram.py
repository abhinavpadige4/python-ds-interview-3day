"""
Problem: Valid Anagram (LeetCode 242)
-------------------------------------
Given two strings s and t, return True if t is an anagram of s.

Approach 1: Counter (dict)
- Count character frequencies in both strings and compare.

Approach 2: Sort
- Sort both strings and compare.

Time:  O(n) for counter, O(n log n) for sort
Space: O(1) (alphabet size) for counter, O(n) for sort
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def is_anagram_sorted(s: str, t: str) -> bool:
    """Alternative: sort both strings and compare."""
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    assert is_anagram_sorted("listen", "silent") is True
    print("All Valid Anagram tests passed.")
