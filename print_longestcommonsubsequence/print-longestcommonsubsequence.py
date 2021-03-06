def longestcommonsubsequence(str1,str2,m,n):
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    i=m
    j=n
    res=""
    while i>0 and j>0:
        if str1[i-1]==str2[j-1]:
            res+="".join(str1[i-1])
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    return res[::-1]

def all_longest_common_subsequences(self, s, t):
	    MAX=100
	    dp=[[-1 for i in range(MAX)] for i in range(MAX)]
	    def lcs(str1, str2, len1, len2, i, j):
	        if (i == len1 or j == len2):
	            dp[i][j] = 0
	            return dp[i][j]
	        if (dp[i][j] != -1):
	            return dp[i][j]
	        ret = 0
	        if (str1[i] == str2[j]):
	            ret = 1 + lcs(str1, str2, len1, len2, i + 1, j + 1)
            else:
                ret = max(lcs(str1, str2, len1, len2, i + 1, j),
                  lcs(str1, str2, len1, len2, i, j + 1))
            dp[i][j] = ret
            return ret
        def printAll(str1, str2, len1, len2,cur, indx1, indx2, currlcs,lcslen):
            if (currlcs == lcslen):
                ans.append(cur)
                return
            if (indx1 == len1 or indx2 == len2):
                return
            for ch in range(ord('a'),ord('z') + 1):
                done = False
                for i in range(indx1,len1):
                    if (chr(ch)==str1[i]):
                        for j in range(indx2, len2):
                            if (chr(ch) == str2[j] and dp[i][j] == lcslen-currlcs):
                                new_cur = cur + chr(ch)
                                printAll(str1, str2, len1, len2, new_cur, i + 1, j + 1, currlcs + 1,lcslen)
                                done = True
                                break
                            if (done):
                                break
        len1,len2 = len(s),len(t)
        lcslen = lcs(s, t, len1, len2, 0, 0)
        global ans
        ans=[]
        printAll(s, t, len1, len2, "", 0, 0, 0,lcslen)
        ans.sort()
        w=set()
        pre=[]
        for i in ans:
            if i in w:
                continue
            else:
                pre.append(i)
                w.add(i)
        return pre
            





str1= input()
str2=input()
m=len(str1)
n=len(str2)
print(longestcommonsubsequence(str1,str2,m,n))
