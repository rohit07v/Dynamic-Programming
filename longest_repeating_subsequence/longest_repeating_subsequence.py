def longest_repeating_subsequence(str1,str2,m,n):
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

def printlongest_repeating_subsequence(str1,str2,m,n):
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    
            elif str1[i-1]==str2[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    i=m
    j=n
    res=""
    while i>0 and j>0:
        if str1[i-1]==str2[j-1] and i!=j:
            res+="".join(str1[i-1])
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    return res[::-1]
    



str1=input()
str2=str1[:]
m=len(str1)
n=len(str2)
print(longest_repeating_subsequence(str1,str2,m,n))
print(printlongest_repeating_subsequence(str1,str2,m,n))


#match the alphabets which are opposite in indices
# same as lcs , only if i!=j added condition
# if same indices it means it cannot be repeated

                 
