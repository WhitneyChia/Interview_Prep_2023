"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3


Notes:
1. IF the duplicate only appeared a max of 2 times, this would be simplified to sum(nums) - summation formula(n)
But this won't work if the duplicate CAN appear more than 2 times, i.e. [2, 2, 2, 2]
2. This is actually Floyd's detection algorithm. Each value is a pointer to the next one, i.e. index 0 has a 3, move to
nums[3] and then index 3 will have a pointer to the next.
The solution is the beginning of the cycle, so this is actually a linked list problem.
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # this is linked list cycle, find the entry to the cycle

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        very_slow = 0
        while True:
            very_slow = nums[very_slow]
            slow = nums[slow]
            if slow == very_slow:
                return slow
