"""
Problem: Longest Substring Without Repeating Characters (LeetCode 3)
--------------------------------------------------------------------
Given a string s, find the length of the longest substring without repeating
characters.

Approach: Sliding window with hash map
- Maintain a window [left, right] with all unique chars.
- If s[right] is already in the window, move left past its previous occurrence.
- Track max window size.

Time:  O(n)
Space: O(min(n, alphabet_size))
"""


def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abcdef") == 6
    print("All Longest Substring tests passed.")
