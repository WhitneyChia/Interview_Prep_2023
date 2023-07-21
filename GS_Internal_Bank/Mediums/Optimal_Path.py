"""
Travel from Socal (bottom left) to NY (upper right)
You can only travel north (up) and east (right)
Maximize the values in the path.

[[0, 0, 0, 0, 5],
[0, 1, 1, 1, 0],
[2, 0, 0, 0, 0]]

Notes
1. This should be DP, cannot solve this with a greedy approach.
Consider
[[0, 2, 0, 0, 0],
[0, 1, 1, 10, 0],
[2, 0, 0, 0, 0]]

If you were greedy, you would do 2 -> 0 -> 1 -> 2 and miss out on the 10.

2. Since this is DP, at each step you choose up or down.
We can build a DP array of the same size, and get the maximum you have reaching that point

[[2, 3, 4, 5, 10],
[2, 3, 4, 5, 5],
[2, 2, 2, 2, 2]]
"""


def optimal_path(grid):

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    ROWS, COLS = len(grid), len(grid[0])

    for i in range(1, COLS):
        grid[ROWS-1][i] = grid[ROWS-1][i - 1]

    for row in range(ROWS - 2, -1, -1):
        for col in range(COLS):
            if col == 0:
                grid[row][col] += grid[row+1][col]
            if col > 0:
                grid[row][col] += max(grid[row+1][col], grid[row][col - 1])

    return grid[0][-1]


if __name__ == "__main__":

    test_1 = [[0, 0, 0, 0, 5], [0, 1, 1, 1, 0], [2, 0, 0, 0, 0]]
    assert optimal_path(test_1) == 10

    test_2 = [[1, 3, 2, 0, 2, 1, 8], [3, 4, 1, 2, 0, 1, 1], [1, 1, 1, 2, 3, 2, 1], [1, 0, 1, 1, 4, 2, 1]]
    assert optimal_path(test_2) == 25

    test_3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert optimal_path(test_3) == 0

    test_4 = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]
    assert optimal_path(test_4) == 8

    test_5 = [[]]
    assert optimal_path(test_5) == 0
