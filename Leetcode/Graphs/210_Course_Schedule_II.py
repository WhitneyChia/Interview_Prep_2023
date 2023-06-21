"""
https://leetcode.com/problems/course-schedule-ii

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course
bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Notes:
1. Set up a map of indegrees, and also adj list for adj_list[src].append(dest)
    So taking course src, possibly opens up the courses in dest
2. The other condition of course, is if dest has another prerequisite, that's why you must also track indegrees
3. It can be added to courses once indegrees reaches 0 for the course
4. whether or not it is possible, simply check that course order size is the same as the number of courses
"""
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Khan's algorithm
        adj_list = collections.defaultdict(list)
        indegrees = {}

        for prereq in prerequisites:
            adj_list[prereq[1]].append(prereq[0])
            if prereq[0] in indegrees:
                indegrees[prereq[0]] += 1
            else:
                indegrees[prereq[0]] = 1

        courses_queue = collections.deque([course for course in range(numCourses) if course not in indegrees])
        course_order = []

        while courses_queue:
            course_can_take = courses_queue.popleft()
            course_order.append(course_can_take)
            for future_course in adj_list[course_can_take]:
                indegrees[future_course] -= 1
                if indegrees[future_course] == 0:
                    courses_queue.append(future_course)

        return course_order if len(course_order) == numCourses else []
