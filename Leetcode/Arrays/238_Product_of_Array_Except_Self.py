"""
https://leetcode.com/problems/product-of-array-except-self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

NOTE:
Use two arrays that are cumulative products
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Left to Right cumulative product
        L_TO_R = [None for i in range(len(nums))]

        # Right to Left cumulative product
        R_TO_L = [None for i in range(len(nums))]

        curr_l_to_r = nums[0]
        L_TO_R[0] = nums[0]
        for i in range(1, len(nums)):
            L_TO_R[i] = nums[i] * curr_l_to_r
            curr_l_to_r = L_TO_R[i]

        curr_r_to_l = nums[len(nums) - 1]
        R_TO_L[len(nums) - 1] = nums[len(nums) - 1]
        for j in range(len(nums) - 2, -1, -1):
            R_TO_L[j] = nums[j] * curr_r_to_l
            curr_r_to_l = R_TO_L[j]

        res = [None for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                res[i] = R_TO_L[i + 1]
            elif i == len(nums) - 1:
                res[i] = L_TO_R[i - 1]
            else:
                res[i] = L_TO_R[i - 1] * R_TO_L[i + 1]

        return res


