"""
https://leetcode.com/problems/restore-ip-addresses

A valid IP address consists of exactly four integers separated by single dots. Each integer is
between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312"
and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be
formed by inserting dots into s. You are not allowed to reorder or remove any digits in s.
You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []

        if len(s) > 12:
            return res

        def backtrack(i, dots, curIp):
            if dots == 4 and i == len(s):
                # we want to remove the extra dot at the end
                res.append(curIp[:-1])
                return

            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curIp + s[i:j + 1] + ".")

        backtrack(0, 0, "")
        return res

