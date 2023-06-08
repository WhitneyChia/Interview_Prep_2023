"""
https://leetcode.com/problems/n-queens-ii/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

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


class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        posDiag = set()
        negDiag = set()
        count = 0

        def backtrack(row):
            if row == n:
                nonlocal count
                count += 1
                return

            for col in range(n):
                if col in cols or (row - col) in negDiag or (row + col) in posDiag:
                    continue

                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        backtrack(0)
        return count
