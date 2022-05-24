def count(arr,sum1):
    n=len(arr)
    dp=[[0 for i in range(sum1+1)]for j in range(n+1)]
    for i in range(n+1):
       
        
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,sum1+1):

            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j-arr[i-1]]+dp[i-1][j]
    return dp[n][sum1]


def count_rec(arr,sum1):
    def rec(i,s):
        if i>=len(arr):
            if s==diff:
                return 1
            return 0
        return rec(i+1,s-arr[i])+rec(i+1,s+arr[i])
    return rec(0,0)




arr=[1,1,2,3]
diff=1
sumx=sum(arr)
sum1=(diff+sumx)//2
print(count(arr,sum1))
print(count_rec(arr,sum1))
