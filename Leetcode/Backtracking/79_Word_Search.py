"""
https://leetcode.com/problems/word-search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        ROWS, COLUMNS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # base case word found, past the index
            if i == len(word):
                return True
            # base case OOB
            if r < 0 or c < 0 or r >= ROWS or c >= COLUMNS:
                return False
            # base case went backwards or not the letter
            if (r, c) in path or board[r][c] != word[i]:
                return False

            path.add((r, c))
            # go in all 4 directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for row in range(ROWS):
            for column in range(COLUMNS):
                if dfs(row, column, 0):
                    return True

        return False
