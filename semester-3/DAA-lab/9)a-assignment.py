import numpy as np
from scipy.optimize import linear_sum_assignment as linSum

def assignment(matrix):
    row, col = linSum(matrix)
    lowBound = matrix[row, col].sum()
    bestA = list(zip(row, col))
    bestC = lowBound
    pQueue = [(lowBound, bestA)]
    while pQueue:
        curBound, curA = pQueue.pop(0)
        task = next((task for task in range(len(matrix)) if task not in [row for row, _ in curA]), None)
        if task is None:
            if curBound < bestC:
                bestA = curA
                bestC = curBound
        else:
            for agent in range(len(matrix)):
                if all(agent != assAgent for _, assAgent in curA):
                    new = curBound + matrix[task, agent]
                    if new < bestC:
                        newAss = curA + [(task, agent)]
                        pQueue.append((new, newAss))
    return bestA, bestC

matrix = np.array([
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
])
bestA, bestC = assignment(matrix)

print("Best Assignment:", bestA)
print("Best Cost:", bestC)
