"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

NOTES
This is simply, counting the connected components of a graph.
Probably the best way that is generalizable is using DFS.

Using recursion, we can go in all 4 directions and mark where we have visited already by just changing the value to "x"
Base cases are key here to stop recursion, out of bounds and something not being land.

Understand this pattern, it comes up very often.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        def dfs(row, col):

            # OOB
            if row < 0 or col < 0:
                return

            # OOB
            if row == ROWS or col == COLS:
                return

            # Not Land or already visited
            if grid[row][col] != "1":
                return

            # visit the land
            grid[row][col] = "x"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1

        return num_islands
