"""
Problem: Valid Parentheses (LeetCode 20)
-----------------------------------------
Given a string s containing just '(', ')', '{', '}', '[' and ']', determine
if the input string is valid.

Approach: Stack
- Push opening brackets onto the stack.
- On a closing bracket, pop and check it matches.
- Valid iff stack is empty at the end.

Time:  O(n)
Space: O(n)
"""


def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    assert is_valid("(") is False
    print("All Valid Parentheses tests passed.")
