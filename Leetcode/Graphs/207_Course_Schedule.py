"""
https://leetcode.com/problems/course-schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Notes:
1. Set up a map of indegrees, and also adj list for adj_list[src].append(dest)
    So taking course src, possibly opens up the courses in dest
2. The other condition of course, is if dest has another prerequisite, that's why you must also track indegrees
3. It can be added to courses once indegrees reaches 0 for the course
4. whether or not it is possible, simply check that course order size is the same as the number of courses
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        indegrees = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            if dest in indegrees:
                indegrees[dest] += 1
            else:
                indegrees[dest] = 1

        courses_can_take = deque([course for course in range(numCourses) if course not in indegrees])
        course_order = []

        while courses_can_take:
            course = courses_can_take.popleft()
            course_order.append(course)
            for next_course in adj_list[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    courses_can_take.append(next_course)

        return len(course_order) == numCourses
