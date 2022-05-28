def longestpalindromicsubsequence(str1):
    m=len(str1)
    newstr=str1[::-1]
    n=len(newstr)
    def lps(str1,newstr,m,n):
        dp=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif str1[i-1]==newstr[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]
    return lps(str1,newstr,m,n)
        

def calc_minimum_no_of_deletion_to_get_palindromic_string(str1):
    m=len(str1)
    newstr=str1[::-1]
    n=len(newstr)
    def lps(str1,newstr,m,n):
        dp=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif str1[i-1]==newstr[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]
    return m-lps(str1,newstr,m,n)






str1=input()

print(longestpalindromicsubsequence(str1))
print(calc_minimum_no_of_deletion_to_get_palindromic_string(str1))
