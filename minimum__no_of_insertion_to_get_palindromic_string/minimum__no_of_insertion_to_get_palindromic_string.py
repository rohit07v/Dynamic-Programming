
def minimum__no_of_insertion_to_get_palindromic_string(str1,str2,m,n):
    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return m-dp[m][n]
                






str1=input()
str2=str1[::-1]
m=len(str1)
n=len(str2)
print(minimum__no_of_insertion_to_get_palindromic_string(str1,str2,m,n))
