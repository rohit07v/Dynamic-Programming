import sys
import time
begin=time.time()
def ispalindrome(x):
    return x==x[::-1]


def minPalPartion(string, i, j):
    if i >= j or ispalindrome(string[i:j + 1]):
        return 0
    ans = float('inf')
    for k in range(i, j):
        count = (
            1 + minPalPartion(string, i, k)
            + minPalPartion(string, k + 1, j)
        )
        ans = min(ans, count)
    return ans
 






    

dp=[[-1 for i in range(1001)]for j in range(1001)]

        
def palindromepartitioningmemoization(x,i,j):
    if i>=j:
        return 0
    if ispalindrome(x[i:j+1]):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    ans=sys.maxsize
    for k in range(i,j):
        count=palindromepartitioningmemoization(x,i,k)+palindromepartitioningmemoization(x,k+1,j)+1
        ans=min(ans,count)
    dp[i][j]=ans
    return dp[i][j]



def palindromepartitioning_more_memoized(x,i,j):
    if i>=j:
        return 0
    if ispalindrome(x[i:j+1]):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    ans=sys.maxsize
    for k in range(i,j):
        if dp[i][k]!=-1:
            left=dp[i][k]
        else:
            left=palindromepartitioning_more_memoized(x,i,k)
        if dp[k+1][j]!=-1:
            right=dp[k+1][j]
        else:
            right=palindromepartitioning_more_memoized(x,k+1,j)

                
        count=1+left+right
        ans=min(count,ans)
    dp[i][j]=ans
    
    return dp[i][j]
time.sleep(1)
end=time.time()


x=input()
print(minPalPartion(x,0,len(x)-1))
#print(f"time{end-begin}")
print(palindromepartitioningmemoization(x,0,len(x)-1))
#print(f"time{end-begin}")
#print(palindromepartitioning_more_memoized(x,0,len(x)-1))
print(f"time{end-begin}")
