"""
https://leetcode.com/problems/top-k-frequent-elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Notes
1. Very intuitive way is counter object, then sort by value, and take the top k
    You have to sort here so this is O(nlogn)
2. Another way is, make a max heap where the key is the count
    This improves this to O(klogn)
3. Optimal way, you can get to O(n)
    You can do this by counting first but also initializing an array of size len(nums) + 1
    Then, the frequency is the index and the list of values are at that index that have that frequency.
    Iterate backwards and keep taking until you reach k
"""
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = dict(Counter(nums))
        frequency = [[] for i in range(len(nums) + 1)]

        for num, count in counter.items():
            frequency[count].append(num)

        res = []

        for i in range(len(frequency) - 1, 0, - 1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
