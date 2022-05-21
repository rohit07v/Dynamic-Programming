def knapsack(w,wt,val,n):
    if n==0 or w==0:
        return 0
    if wt[n-1]>w:
        return knapsack(w,wt,val,n-1)
    else:
        return max(val[n-1]+knapsack(w-wt[n-1],wt,val,n-1),knapsack(w,wt,val,n-1))

def knapsack_memoize(w,wt,val,n):
    if n==0 or w==0:
        return 0
    if dp[n][w]!=-1:
        return dp[n][w]

    if wt[n-1]>w:
        dp[n][w]=knapsack_memoize(w,wt,val,n-1)
        return dp[n][w]

    else:
        dp[n][w]=max(val[n-1]+knapsack_memoize(w-wt[n-1],wt,val,n-1),knapsack_memoize(w,wt,val,n-1))
        return dp[n][w]

def knapsack_topdown(w,wt,val,n):
    dp=[[0 for i in range(w+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
    return dp[n][w]



val = [60,100,120]                        
wt = [10,20,30]
w = 50
n=len(val)
dp=[[-1 for i in range(w+1)]for j in range(n+1)]
print(knapsack(w,wt,val,n))
print(knapsack_memoize(w,wt,val,n))
print(knapsack_topdown(w,wt,val,n))
