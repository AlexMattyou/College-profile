def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    comb = [[]] + [[] for _ in range(amount)]
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                comb[i] = comb[i - coin] + [coin]
                
    return dp[-1] if dp[-1] != float('inf') else -1, comb[-1]

coins = [1, 2, 3]
amount = 10
minCoins, coinComb = coinChange(coins, amount)
print(f"Minimum coins needed: {minCoins}")
print(f"Coin combination: {coinComb}")
