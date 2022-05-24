def havesubset(arr,sumx,n):
    if sumx==0:
        return True
    if n==0 and sumx!=0 :
        return False
    if arr[n-1]>sumx:
        return havesubset(arr,sumx,n-1)
    return havesubset(arr,sumx-arr[n-1],n-1) or havesubset(arr,sumx,n-1)



def equalsum(arr,n):
    sumx=sum(arr)
    if sumx%2!=0:
        return False
    return havesubset(arr,sumx//2,n)




def equalsum_dp(arr,n):
    sumx=sum(arr)
    if sumx%2!=0:
        return False
    dp=[[False for i in range(sumx+1)]for j in range(n+1)]
    for i in range(0,n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,(sumx//2)+1):
            dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][sumx//2]
    
        

arr=list(map(int,input().split()))

n=len(arr)

print(equalsum(arr,n))
#print(equalsum_dp(arr,n))





