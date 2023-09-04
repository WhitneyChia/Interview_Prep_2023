"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly
one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""
from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # this is essentially minimum spanning tree and we can use Prim's for it
        # since we are not given edge, we make an edge from each node to the other nodes
        nodes = len(points)
        adj_list = {}
        for i in range(nodes):
            adj_list[i] = []

        for i in range(nodes):
            for j in range(nodes):
                if j == i:
                    continue
                src_x, src_y = points[i]
                dest_x, dest_y = points[j]
                distance = abs(src_x - dest_x) + abs(src_y - dest_y)
                adj_list[i].append([distance, j])
                adj_list[j].append([distance, i])

        visited = set()
        result = 0
        min_heap = [[0, 0]]  # [distance, dest]

        while min_heap:
            if len(visited) == nodes:
                return result

            distance, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            result += distance

            for distance, neighbor in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, [distance, neighbor])

        return result