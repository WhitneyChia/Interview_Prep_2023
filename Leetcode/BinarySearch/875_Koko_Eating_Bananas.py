"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Notes
Imagine the brute force way here first. One key that they tell you is that len(p) <= h.
If that weren't so, it would be impossible to finish the bananas no matter the k.
Given that len(p) <= h is true, we can develop a search space.

The slowest possible would be 1, doesn't eat all of the bananas in time.
The fastest possible would be max(piles), since we know if the max can be done in 1 hour, then all the piles also can.

From that we know the search space, so [1, 2, 3..... max(piles)]
The answer is somewhere in there, so if max(piles) = 11 then
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
We need to find the cutoff from not possible to finish in time, to possible to finish in time.
[not possible, not_possible, not_possible, not_possible, possible, possible, ......]
                                               FIND THIS CUTOFF

We could do this iteratively, start at 1 and test, then 2, then 3 etc. until we find it.
But binary searching this instead is more efficient.

We turn this from O(max(p) * p) since for each p up to the max we need to check all piles if possible.
Into O(log(max(p)) * p) with binary search.
"""


from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        L, R = 1, res

        while L <= R:
            mid = L + (R - L) // 2
            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p / mid)

            if hours_needed <= h:
                R = mid - 1
                res = mid
            else:
                L = mid + 1

        return res