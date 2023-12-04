def subsetSum(numbers, target, partial=[], partialSum=0):
    if partialSum == target:
        print(partial)
    if partialSum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        subsetSum(remaining, target, partial + [n], partialSum + n)

numbers = [3, 9, 6, 5, 1, 8]
target = 14
print("Target sum:",target,'\nCombinations:')
subsetSum(numbers, target)
