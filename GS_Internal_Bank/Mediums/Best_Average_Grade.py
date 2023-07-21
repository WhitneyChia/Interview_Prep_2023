"""
Given a list of student test scores, find the best average grade.
Each student may have more than one test score in the list.

Complete the bestAverageGrade function in the editor below.

Example 1:
[["Bobby", "87"], ["Charles", "100"], ["Eric", "64"], ["Charles", "22"]]

87 for Bobby is the highest
"""


def bestAverageGrade(scores):

    # Keep a running dictionary {name: (total, score_count)}
    averages = {}

    for name, score in scores:
        if name in averages:
            averages[name][0] += int(score)
            averages[name][1] += 1
        else:
            averages[name] = [int(score), 1]

    max_average = 0
    for total, score_count in averages.values():
        max_average = max(max_average, (total // score_count))

    return max_average


if __name__ == "__main__":

    test = [["Bobby", "87"], ["Charles", "100"], ["Eric", "64"], ["Charles", "22"]]

    print(bestAverageGrade(test))