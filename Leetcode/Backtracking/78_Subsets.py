"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Notes
For these types of questions, imagine a decision tree. You either take the number or don't take the number
For example: given [1, 2, 3]

                  root
               /        \
              [1]        []
            /     \      /    \
        [1,2]    [1]    [2]    []
       /   \     /  \   /  \   /  \
[1,2,3] [1,2] [1,3][1][2,3][2][3] []     <- at the bottom level of the tree, you will have all of the sets

We can use recursion/backtracking for this.
Recursively call the backtracking function by taking the number.
Then backtrack by removing that number, and calling backtrack function again for the other side of the tree.

Base case is simply, you reached the bottom of the tree.
Do note curr_set.copy(), be careful when using backtracking since you might modify solutions, so we append a copy at that time.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []
        nums_size = len(nums)

        def backtrack(index, curr_set, subsets):

            if index == nums_size:
                subsets.append(curr_set.copy())
                return

            # Left side of tree, choose it
            curr_set.append(nums[index])
            backtrack(index + 1, curr_set, subsets)

            # Right side of tree, don't choose it
            curr_set.pop()
            backtrack(index + 1, curr_set, subsets)

        backtrack(0, [], subsets)

        return subsets
