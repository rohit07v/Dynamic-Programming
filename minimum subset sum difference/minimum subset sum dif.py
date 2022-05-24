import sys
def subsetsum(arr,sumx):
    n=len(arr)
    dp=[[False for i in range(sumx+1)]for j in range(n+1)]
    
    for i in range(n+1):
        
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,sumx+1):
            if arr[i-1]>=sumx:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
    diff=sys.maxsize
    for i in range(sumx//2,-1,-1):
        if dp[n][i]==True:
            diff=sumx-(2*i)
            break
    return diff




arr=[1,2,7]
sumx=sum(arr)
print(subsetsum(arr,sumx))
                
