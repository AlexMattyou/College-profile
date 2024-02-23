def minCoins(coins,amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    coinUsed = [[] for _ in range(amount+1)]
    
    for coin in coins:
        for i in range(coin, amount+1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[coin] + 1
                coinUsed[i] = coinUsed[i - coin] + [coin]
                
    if dp[amount] != 2 or coinUsed[amount] != 
                
    return dp[amount], coinUsed[amount]


coins = [1,2,4,5]
amount = 8

result = minCoins(coins,amount)
print(result)