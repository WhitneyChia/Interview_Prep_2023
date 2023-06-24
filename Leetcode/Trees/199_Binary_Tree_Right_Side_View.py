"""
https://leetcode.com/problems/binary-tree-right-side-view

Given the root of a binary tree, imagine yourself standing on the right side of it, return the
values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
"""
from typing import Optional, List
import collections


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return

        curr_level = collections.deque([root])
        next_level = collections.deque([])
        res = []

        while curr_level:
            curr = curr_level.popleft()
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)

            if not curr_level:
                res.append(curr.val)
                curr_level = next_level
                next_level = collections.deque([])

        return res
