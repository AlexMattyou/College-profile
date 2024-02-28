def cryptoSolver(p):
    out = {}
    chars = set(c for w in p for c in w)
    if len(chars) > 10:
        raise ValueError("The number of unique characters exceeds 10.")
    digits = {}

    def isValid():
        return all((w[0] not in digits) or (digits[w[0]] != 0) for w in p)

    def convNum(word):
        return int("".join(str(digits[c]) for c in word))

    def backtrack(index):
        if index == len(chars):
            return sum(convNum(w) for w in p[:-1]) == convNum(p[-1])
        char = list(chars)[index]
        for digit in range(10):
            if digit not in digits.values():
                digits[char] = digit
                if isValid() and backtrack(index + 1):
                    return True
                digits.pop(char)
        return False

    if backtrack(0):
        SAssignments = sorted(digits.items(), key=lambda x: x[0])
        for c, value in SAssignments:
            out[c] = value
    else:
        print("No solution found.")
    return out


def display(p):
    print(f"{p[0]} + {p[1]} = {p[2]}")
    ans = cryptoSolver(p)
    for i in ans:
        print(i, "= ", ans[i])
    print()

puzzle1 = ["TWO", "TWO", "FOUR"]
puzzle2 = ["SEND", "MORE", "MONEY"]
puzzle3 = ["CROSS", "ROADS", "DANGER"]

display(puzzle1)
display(puzzle2)
display(puzzle3)

