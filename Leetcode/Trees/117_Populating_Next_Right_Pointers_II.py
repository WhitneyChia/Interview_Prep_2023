"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point
to its next right node, just like in Figure B. The serialized output is in level order as connected by the next
pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # level order traversal
        if not root:
            return

        current_level = collections.deque([root])
        next_level = collections.deque([])

        while current_level:
            curr = current_level.popleft()
            if current_level:
                curr.next = current_level[0]

            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)

            if not current_level:
                current_level = next_level
                next_level = collections.deque([])

        return root
