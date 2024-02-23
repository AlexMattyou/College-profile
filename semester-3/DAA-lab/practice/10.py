def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a table to store the maximum value for each subproblem
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight exceeds the capacity, skip it
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Choose the maximum value between including and excluding the current item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    # Backtrack to find the items included in the optimal solution
    included_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i)
            w -= weights[i - 1]
        i -= 1

    # Return the maximum value and the list of included items
    return dp[n][capacity], included_items

# Given instance of the problem
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Solve the knapsack problem
max_value, included_items = knapsack(weights, values, capacity)

# Print the optimal solution
print("Optimal Solution:")
print("Maximum Value:", max_value)
print("Included Items:", included_items)


'''
output:

Optimal Solution:
Maximum Value: 7
Included Items: [2, 1]

'''