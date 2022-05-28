def minimum_number_of_insertion_and_deletion(str1,str2,m,n):
    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print("minimum_number_of_deletion",m-dp[i][j])
    print("minimum_number_of_insertion",n-dp[i][j])


str1=input()
str2=input()
m=len(str1)
n=len(str2)
minimum_number_of_insertion_and_deletion(str1,str2,m,n)
