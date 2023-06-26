"""
https://leetcode.com/problems/network-delay-time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel
times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to
receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = collections.defaultdict(list)

        for time in times:
            src, dest, weight = time[0], time[1], time[2]
            adj_list[src].append((dest, weight))

        minHeap = [(0, k)]
        shortest_paths = {}

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in shortest_paths:
                continue

            shortest_paths[node] = weight

            for neighbor in adj_list[node]:
                node2, weight2 = neighbor[0], neighbor[1]
                heapq.heappush(minHeap, (weight + weight2, node2))

        return max(shortest_paths.values()) if len(shortest_paths) == n else -1
