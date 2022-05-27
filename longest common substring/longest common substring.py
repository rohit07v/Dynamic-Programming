

def longestcommonsubstring(str1,str2,m,n):
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    result =0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                result = max(result , dp[i][j])
            else:
                dp[i][j]=0
    return result
# we used result coz substring can exist anywhere in between




str1=input()
str2=input()
m=len(str1)
n=len(str2)
print(longestcommonsubstring(str1,str2,m,n))
