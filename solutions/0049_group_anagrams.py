"""
Problem: Group Anagrams (LeetCode 49)
-------------------------------------
Given an array of strings, group anagrams together.

Approach: Sort each word as a key
- Two words are anagrams iff their sorted forms are equal.
- Use a dict mapping sorted_word -> list of original words.

Time:  O(n * k log k) where n = #words, k = max word length
Space: O(n * k)
"""
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())


if __name__ == "__main__":
    out = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    out.sort(key=lambda g: sorted(g)[0])
    assert out == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All Group Anagrams tests passed.")
