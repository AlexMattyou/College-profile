from itertools import combinations

def knapsack(i, w, maxW):
    optVal, optComb = 0, []
    for r in range(1, len(i) + 1):
        for comb in combinations(range(len(i)), r):
            totalW = sum(w[x] for x in comb)
            if totalW <= maxW and totalW > optVal:
                optVal, optComb = totalW, [i[x] for x in comb]
    return optComb, optVal

i = ['I1', 'I2', 'I3']
w = [10, 20, 30]
maxW = 50
print(knapsack(i, w, maxW))
