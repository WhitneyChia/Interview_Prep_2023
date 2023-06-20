"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Note:
neetcode explains it better than I ever could.
https://www.youtube.com/watch?v=q6IEA26hvXc
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Always make A the smaller sized array
        if len(A) > len(B):
            A, B = B, A

        L, R = 0, len(A) - 1

        while True:
            i = (L + R) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            # Correctly partitioned
            if Aleft <= Bright and Bleft <= Aright:
                # odd length
                if total % 2:
                    return min(Aright, Bright)
                # even length
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # Keep binary searching
            elif Aleft > Bright:
                R = i - 1
            else:
                L = i + 1
