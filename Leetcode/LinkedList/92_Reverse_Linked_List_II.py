"""
https://leetcode.com/problems/reverse-linked-list-ii

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head.next:
            return head

        dummy_node = ListNode()
        curr = dummy_node
        dummy_node.next = head

        counter = 0

        # Separate into 3 lls
        while curr:
            if counter == left - 1:
                left_partition_end = curr
                middle_partition_start = curr.next
                curr = curr.next
                left_partition_end.next = None

            elif counter == right:
                middle_partition_end = curr
                right_partition_start = curr.next
                curr = curr.next
                middle_partition_end.next = None

            else:
                curr = curr.next

            counter += 1

        # Reverse the middle
        new_middle_partition_start = self.reverse_ll(middle_partition_start)

        left_partition_end.next = new_middle_partition_start

        curr = new_middle_partition_start
        while curr:
            if not curr.next:
                curr.next = right_partition_start
                break
            curr = curr.next

        return dummy_node.next

    def reverse_ll(self, head):

        prev = None
        curr = head

        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        return prev
