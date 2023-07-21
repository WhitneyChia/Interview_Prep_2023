"""
https://leetcode.com/problems/generate-parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parens = []

        def paren_helper(starting_point, n, count):

            if self.terminate_early(starting_point, n, count):
                return

            if len(starting_point) == n * 2:
                if self.is_valid_parens(starting_point):
                    parens.append(starting_point)
                    return
                else:
                    return

            paren_helper(starting_point + "(", n, count + 1)
            paren_helper(starting_point + ")", n, count - 1)

            return parens

        return paren_helper("", n, 0)

    def terminate_early(self, parens, n, count):
        remaining_spaces = n * 2 - len(parens)
        if count < 0:
            return True
        if count + remaining_spaces < 0:
            return True
        return False

    def is_valid_parens(self, parens):
        counter = 0
        for paren in parens:
            if paren == "(":
                counter += 1
            if paren == ")":
                counter -= 1
                if counter < 0:
                    return False

        return counter == 0
