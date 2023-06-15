"""
https://leetcode.com/problems/diameter-of-binary-tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Notes
1. One key here is that the biggest diameter does not always pass through the root.
2. One thing we know how to do is calculate the height of a tree.
3. From that, we also know how to calculate the height of the left tree and right tree.
4. We need to track both the height at a node -> max(left, right)
5. And the diameter at that node, which is simply left + 1 + right + 1 -> 2 + left + right
6. Continually track the largest diameter seen and return that
"""
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, 2 + left + right)
            return 1 + max(left, right)

        dfs(root)
        return res
