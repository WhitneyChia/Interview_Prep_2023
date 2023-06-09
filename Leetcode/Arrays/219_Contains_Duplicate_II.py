"""
https://leetcode.com/problems/contains-duplicate-ii

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in
the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Notes
This is sliding window technique, where your max window is k + 1 since length of 4 = index 3 - index 0 = 3.
Sliding window but we use a set to track what we've seen and is in our current window.
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False