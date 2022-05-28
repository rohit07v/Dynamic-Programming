def shortestcommonsupersequence(str1,str2,m,n):
    def lcs(str1,str2,m,n):
        
        dp=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        final_string=""
        i=m
        j=n
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                final_string+="".join(str1[i-1])
                i-=1
                j-=1
            else:
                if dp[i-1][j]>dp[i][j-1]:
                    final_string+="".join(str1[i-1])
                    i-=1
                else:
                    final_string+="".join(str2[j-1])
                    j-=1
        while i>0:
            final_string+="".join(str1[i-1])
            i-=1
        while j>0:
            final_string+="".join(str2[j-1])
            j-=1
        return final_string[::-1]
    return lcs(str1,str2,m,n)
            
        
            




str1=input()
str2=input()
m=len(str1)
n=len(str2)
print(shortestcommonsupersequence(str1,str2,m,n))
