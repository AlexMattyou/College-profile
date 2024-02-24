def find_combinations(numbers, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(numbers)):
            if numbers[i] > target:
                break
            backtrack(i, target - numbers[i], path + [numbers[i]])

    result = []
    backtrack(0, target, [])
    return result

numbers = [1, 2, 5, 6, 8]
target = 9

combinations = find_combinations(numbers, target)
print("Combinations of numbers that sum up to", target, "are:")
for combination in combinations:
    print(combination)


'''
output:

[1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 2]
[1, 1, 1, 1, 1, 2, 2]
[1, 1, 1, 1, 5]
[1, 1, 1, 2, 2, 2]
[1, 1, 1, 6]
[1, 1, 2, 5]
[1, 2, 2, 2, 2]
[1, 2, 6]
[1, 8]
[2, 2, 5]


'''