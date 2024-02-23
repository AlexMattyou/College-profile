def min_coins(coins, amount):
    # Initialize dp array with a large value
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Zero coins needed to make zero amount

    # Initialize array to store coin used for each amount
    coin_used = [[] for _ in range(amount + 1)]

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp array for each amount from coin to amount
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]

    return dp[amount], coin_used[amount]

# Given coins denominations and amount
coins = [1, 2, 4, 5]
amount = 8

# Find optimal number of coins and sequence of coins used
num_coins, coin_sequence = min_coins(coins, amount)

# Print the result
print("Optimal number of coins:", num_coins)
print("Sequence of coins used:", coin_sequence)


'''
output:

Optimal number of coins: 2
Sequence of coins used: [4, 4]

'''
