"""
https://leetcode.com/problems/coin-change

You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

NOTE
This is a classical dynamic programming problem
1. Since this utilizes min, we initialize a 1-d array at a high value from 0 - amount
2. We instantiate dp[0] as 0, first row usually 0 and we know we only need 0 coins to make an amount of zero
3. We go bottom up and solve each amount up to the amount, 1 -> amount
4. Every time we are left with a choice of not taking the coin or taking the coin.
5. dp[a] can keep changing since we evaluate it for every coin.
6. Keeping the dp array prevents us from solving things multiple times.
    amount = 7
    coins = 1, 3, 5
    at 7, we can choose a 3 coin so 1 + d[7- 3] -> 1 + dp[4] which we have already solved.
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if (a - coin) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != float('inf') else -1