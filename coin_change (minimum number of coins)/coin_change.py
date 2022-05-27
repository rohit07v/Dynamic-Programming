import sys
def coin_change(coins,W):

    n= len(coins)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0:
                dp[i][j]=(sys.maxsize)-1
    for j in range(1,W+1):
        if j% coins[0]==0:
            dp[1][j]=j//coins[0]
        else:
                
            dp[1][j]=(sys.maxsize)-1
            
    for i in range(2,n+1):
        for j in range(1,W+1):
            if j >= coins[i-1]:
                a1 = 1 + dp[i][j - coins[i - 1]]
                a2 = dp[i-1][j]
                ans = min(a1,a2)
                dp[i][j] = ans
            else:
                dp[i][j] = dp[i-1][j]
    
    if dp[n][W]==sys.maxsize-1:
        return -1
    else:
        return dp[n][W]
        



coins = [25,10,5]
sumx = 30
print(coin_change(coins,sumx))


