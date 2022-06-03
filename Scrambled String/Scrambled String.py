
def isScrambled(str1,str2):
    if len(str1)!=len(str2):
        return False
    if not len(str1):
        return True
    if str1==str2:
        return True
    if sorted(str1)!=sorted(str2):
        return False
    for k in range(1,len(str1)):
        if (isScrambled(str1[:k],str2[:k]) and isScrambled(str1[k:],str2[k:])):
            return True
        if (isScrambled(str1[-k:],str2[:k]) and isScrambled(str1[:-k],str2[k:])):
            return True
    return False







def isScrambled_memoized(str1,str2):
    if len(str1)!=len(str2):
        return False
    if dp[m][n]!=-1:
        return dp[i][j]
    if not len(str1):
        return True
    if str1==str2:
        return True
    if sorted(str1)!=sorted(str2):
        return False
    for k in range(1,len(str1)):
        if (isScrambled(str1[:k],str2[:k]) and isScrambled(str1[k:],str2[k:])):
            dp[m][n]=True
            return dp[m][n]
        if (isScrambled(str1[-k:],str2[:k]) and isScrambled(str1[:-k],str2[k:])):
            dp[m][n]=True
            return dp[m][n]
        
    dp[m][n]=False
    return dp[m][n]



str1=input()
str2=input()
m=len(str1)
n=len(str2)
dp=[[-1 for i in range(len(str2)+1)]for j in range(len(str1)+1)]
if isScrambled_memoized(str1,str2):
    print("TRUE")
else:
    print("FALSE")
