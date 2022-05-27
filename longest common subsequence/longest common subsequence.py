
def lcs(str1,str2,m,n):
    if n==0 or m==0:
        return 0
    if str1[m-1] == str2[n-1]:
        return 1+lcs(str1,str2,m-1,n-1)
    else:
        return max(lcs(str1,str2,m,n-1),lcs(str1,str2,m-1,n))

def lcs_dp(str1,str2,m,n):
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
    






str1=input()
str2=input()
m=len(str1)
n=len(str2)

print(lcs(str1,str2,m,n))
print(lcs_dp(str1,str2,m,n))
