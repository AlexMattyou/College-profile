def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# example usage
print(factorial(5)) # output: 120
print(factorial(0)) # output: 1
print(factorial(-3)) # output: "Factorial is not defined for negative numbers"