# INITIALIZATION OF TABLE 

# 0 1 2 3 4 5 6
# 1 T F F F F F 
# 2 T F F F F F 
# 3 T F F F F F 




def subsetsum(arr,sumx,n):
    if sumx==0:
        return True
    if n<0 or sumx<0:
        return False
    include = subsetsum(arr,sumx-arr[n-1],n-1)
    exclude=subsetsum(arr,sumx,n-1)
    return exclude or include


def subsetsum_memoize(arr,sumx,n):
    if sumx==0:
        return True
    if n<0 or sumx<0:
        return False
    if dp[n][sumx]!=-1:
        return True
    include = subsetsum(arr,sumx-arr[n-1],n-1)
    exclude=subsetsum(arr,sumx,n-1)
    dp[n][sumx]=include or exclude
    return dp[n][sumx]

def subsetsum_topdown(arr,sumx):
    n=len(arr)
    dp=[[False for x in range(sumx+1)]for y in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,sumx+1):
            
            
            if arr[i-1]<=sumx:
                dp[i][j]=(dp[i-1][j-arr[i-1]]) or (dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][sumx]




arr=[int(ele) for ele in input().strip().split(" ")]
sumx=int(input())
n=len(arr)
dp=[[-1 for i in range(sumx+1)]for j in range(n+1)]
print(subsetsum(arr,sumx,n))
print(subsetsum_memoize(arr,sumx,n))
print(subsetsum_topdown(arr,sumx))
