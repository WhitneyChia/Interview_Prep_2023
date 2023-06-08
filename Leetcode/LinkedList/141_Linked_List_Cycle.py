"""
https://leetcode.com/problems/linked-list-cycle/description/
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Notes
This is a fast pointer and a slow pointer in a linked list.
If the two ever meet, that is only possible if it is a cycle.
Just catch AttributeError and return false, if there is no next, means there is no cycle and the linkedlist ends
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow_runner = fast_runner = head

        while slow_runner:
            try:
                slow_runner = slow_runner.next
                fast_runner = fast_runner.next.next
                if slow_runner == fast_runner:
                    return True
            except AttributeError:
                return False
