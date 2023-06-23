"""
Implementation of Dijkstra's algorithm.

Given a connected graph represented by a list of edges, where
edge[0] = src, edge[1] = dst, and edge[2] = weight.
find the shortest path from src to every other node in the graph.
There are n nodes in the graph.
O(E * logV), O(E * logE) is also correct

This uses a min heap.
"""
import heapq


def shortest_path(edges, n, src):

    # Set up
    adj_list = {}
    for i in range(1, n + 1):
        adj_list[i] = []

    for src, dest, weight in edges:
        adj_list[src].append((dest, weight))

    # Track the shortest path to dest nodes
    shortest = {}

    # Set up a min heap to pull the next shortest edge
    min_heap = [(0, src)]
    heapq.heapify(min_heap)

    while min_heap:
        weight_dest, dest = heapq.heappop(min_heap)
        if dest in shortest:
            continue
        shortest[dest] = weight_dest

        for dest2, weight_dest2 in adj_list[dest]:
            if dest2 not in shortest:
                heapq.heappush(min_heap, (weight_dest + weight_dest2, dest2))

    return shortest


if __name__ == "__main__":

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    ans = 2

    print(shortest_path(times, n, k))

    times = [[1, 2, 1]]
    n = 2
    k = 1
    ans = 1

    print(shortest_path(times, n, k))
