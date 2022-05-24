
def findTargetSumWayshelper(arr,total):
    zero_count=0
    for digit in arr:
        if digit==0:
            zero_count+=1
    for i in range(zero_count):
        arr.remove(0)

    dp=[[0 for i in range(total+1)]for j in range(len(arr)+1)]
    for i in range(len(arr)+1):
        dp[i][0]=1
    for i in range(1,len(arr)+1):
        for j in range(1,total+1):
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j-arr[i-1]]+dp[i-1][j]
    return dp[i][j]*pow(2,zero_count)


def findTargetSumWays(arr,n,target):
    if sum(arr)==0:
        return pow(2,n)

    else:
        total = abs(target)+sum(arr)
        if total%2==0:
            total//=2
            return findTargetSumWayshelper(arr,total)
    return 0






arr=[1,0,0,0,0]
target = 1
n=len(arr)
print(findTargetSumWays(arr,n,target))
