
def coin_change(coins,sumx):
    n=len(coins)
    dp=[[0 for i in range(sumx+1)]for j in range(n+1)]

    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,sumx+1):
            if coins[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
    return dp[n][sumx]
    





coins = [1,2,3]
sumx = 5

print(coin_change(coins,sumx))
