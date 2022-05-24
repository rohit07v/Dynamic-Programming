mod = 10**9+7
def perfectSum(arr, n, sumx):
        
        dp = [[0 for i in range(sumx + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(sumx + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                dp[i][j]%=mod
        
        return dp[-1][-1] % mod
arr=[9,7,0,3,9,8,6,5,7,6]
sumx=31
n=len(arr)
print(perfectSum(arr,n,sumx))


