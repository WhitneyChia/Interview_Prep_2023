"""
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

NOTES
This is backtracking in the way of either choosing to place a queen down or not for a given square.
The backtracking part is, placing the queen down and moving onto the next row, vs. not and moving onto the next column.

The important insight here is, being able to check if you can or cannot place a queen down.
This is easy for rows and columns, when you place one down add it to a set so you know that row and column is no longer available.
However, you must figure out how to do this for the diagonals.

Imagine a 4x4, positive Diagonal and Negative Diagonal

Negative Diagonal, r-c
   0  1  2  3
0  0 -1 -2 -3
1  1  0 -1 -2
2  2  1  0 -1
3  3  2  1  0

Positive Diagonal, r+c
   0  1  2  3
0  0  1  2  3
1  1  2  3  4
2  2  3  4  5
3  3  4  5  6

Once you see this, you can then check against a set when you can't place a queen down.
When you can place it down, then check case of placing it down, and backtrack, not place it down.
There is clean up to be done when undoing placing it down.
You don't need to call backtrack after cleaning it up since it will pick up on the next iteration in the for loop.
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()
        posDiag = set()
        negDiag = set()
        sols = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                sols.append(copy)
                return

            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue

                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return sols
