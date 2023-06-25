"""
https://leetcode.com/problems/robot-bounded-in-circle

On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        # if robot comes back in 1, 2 or 4 iterations, it is a cycle
        position = [0, 0]
        left_turns = {"N": "W", "W": "S", "S": "E", "E": "N"}
        right_turns = {"N": "E", "W": "N", "S": "W", "E": "S"}
        facing = "N"

        for i in range(4):
            for instruction in instructions:
                if instruction == "L":
                    facing = left_turns[facing]
                elif instruction == "R":
                    facing = right_turns[facing]
                else:
                    if facing == "N":
                        position[1] += 1
                    elif facing == "S":
                        position[1] -= 1
                    elif facing == "E":
                        position[0] += 1
                    else:
                        position[0] -= 1

            if position == [0, 0]:
                return True
