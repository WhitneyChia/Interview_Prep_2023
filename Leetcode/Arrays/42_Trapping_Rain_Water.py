"""
https://leetcode.com/problems/trapping-rain-water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]

Output: 9
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        total_water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] < max_left:
                    total_water += (max_left - height[left])
                max_left = max(height[left], max_left)
                left += 1
            if height[right] <= height[left]:
                if height[right] < max_right:
                    total_water += (max_right - height[right])
                max_right = max(height[right], max_right)
                right -= 1

        return total_water
