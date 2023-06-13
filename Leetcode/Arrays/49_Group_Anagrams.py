"""
https://leetcode.com/problems/group-anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Notes
This solution is simplest but sorting will dominate and you have to sort every word.
One thing of note, to make the sorted string a key, you need to make it a tuple since a list is not hashable.
A tuple is immutable so it is hashable.
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict = defaultdict(list)
        res = []

        for s in strs:
            key = tuple(sorted(s))
            anagrams_dict[key].append(s)

        for k, v in anagrams_dict.items():
            res.append(v)

        return res
