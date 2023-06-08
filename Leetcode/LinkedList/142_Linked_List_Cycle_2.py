"""
https://leetcode.com/problems/linked-list-cycle-ii/
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

NOTES
This uses the cycle detection from leetcode 141 but builds on it.
This works every time but the proof gets a little mathy.

If you consider the cycle as length c, and the distance from the entrance to where slow and fast met as x.
Then, after detecting the cycle, the slow pointer has traveled a distance of p + (c - x) with the remaining distance as x.

If you consider the distance from head to the entrance as p, we need to prove that p = x.

We can do this by starting with the distance that the slow traveled and the fast traveled
We KNOW 2 * slow = fast in terms of distance traveled.
We can represent the slow distance as p + (c - x)
so
2 * (p + (c-x)) = p + c + (c - x)  -> the fast pointer traveled p and made one entire cycle extra
simplify
2p + 2c - 2x = p + 2c - x
2p - 2x = p - x
p - x = 0
p = x

Proves the algorithm is guaranteed
"""
from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # find if there is a cycle
        node_initially_met = self.hasACycle(head)
        if node_initially_met is None:
            return None

        # have a new pointer at head, when slow and new meet, that's the entrance
        new_pointer = head

        while new_pointer:
            if new_pointer == node_initially_met:
                return new_pointer

            new_pointer = new_pointer.next
            node_initially_met = node_initially_met.next

    def hasACycle(self, head) -> ListNode | None:
        slow_pointer = fast_pointer = head

        while slow_pointer:
            try:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next

                if slow_pointer == fast_pointer:
                    return slow_pointer

            except AttributeError:
                return None
