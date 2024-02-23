def minCoins(coins,amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    coinUsed = [[] for _ in range(amount+1)]
    
    for alex in coins:
        for i in range(alex, amount+1):
            if dp[i - alex] + 1 < dp[i]:
                dp[i] = dp[alex] + 1
                coinUsed[i] = coinUsed[i - alex] + [alex]
                
    return dp[amount], coinUsed[amount]


coins = [1,2,4,5]
amount = 8

result = minCoins(coins,amount)
print(result)