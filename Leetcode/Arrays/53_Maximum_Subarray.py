"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

NOTES
The takeaway from this is that this is simply Kadane's algorithm.
When you have a negative prefix, you would never take that, so you would move the left pointer and start summing from the current index.
When you have a positive prefix, you would always take that, so you always take that, so leave the left pointer and keep summing.
All the while tracking the max sum seen so far.

For example:
given: [-2,1,-3,4]
answer here is 4 because:
[-2,1,-3,4] at index 0, your max subarray sum is just the 0th element
[-2,1,-3,4] at index 1, you have a -2 prefix, never include that, 1 is the max
[-2,1,-3,4] at index 2, you have a positive prefix 1, include the 1, and add -3
[-2,1,-3,4] at index 3, you have a negative prefix (1 + -3 -> -2), it is equivalent to [-2, 4]. Don't include the -2 and start with 4.

"""
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        curr = max_sum = nums[0]

        for num in nums[1:]:
            if curr < 0:
                curr = num
            else:
                curr += num
            max_sum = max(curr, max_sum)

        return max_sum

