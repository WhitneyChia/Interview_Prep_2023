"""
https://leetcode.com/problems/valid-parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Note
Use a stack to track if valid or not
"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        parens_mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for paren in s:

            # Case of close paren without any open parens
            if paren in parens_mapping and not stack:
                return False

            # case of close paren with a mismatching open paren
            if paren in parens_mapping and stack[-1] != parens_mapping[paren]:
                return False

            # case of matching paren, eliminate
            if paren in parens_mapping and stack[-1] == parens_mapping[paren]:
                stack.pop()
                continue

            stack.append(paren)

        return len(stack) == 0
