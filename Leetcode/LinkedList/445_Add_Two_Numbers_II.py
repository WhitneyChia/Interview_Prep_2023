"""
https://leetcode.com/problems/add-two-numbers-ii

You are given two non-empty linked lists representing two non-negative integers. The most
significant digit comes first and each of their nodes contains a single digit. Add the two numbers and
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
"""
from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self.reverse_ll(l1)
        l2 = self.reverse_ll(l2)
        dummy_node = ListNode(-1)
        curr_res = dummy_node
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry

            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0

            curr_res.next = ListNode(total)
            curr_res = curr_res.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverse_ll(dummy_node.next)

    def reverse_ll(self, head):

        prev = None
        curr = head

        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        return prev
