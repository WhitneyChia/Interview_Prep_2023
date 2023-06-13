"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list

Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Notes
Two intuitive ways to solve this.
1. Iterate through the list one time to get the length. Figure out where to stop, and then change the next pointer to next.next.
2. Way that catches more edge cases, is two pointers but with a gap of size n.
    dummy_prev helps edge cases, remember this technique
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # two pointers, trailing by n

        if not head.next:
            return None

        dummy_prev = ListNode(-1)
        dummy_prev.next = head
        left = dummy_prev
        right = head
        counter = 0

        while counter < n:
            right = right.next
            counter += 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy_prev.next
