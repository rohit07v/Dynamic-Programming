from sys import maxsize as MAX_VALUE
def countstepsto1(n):
    if n==1:
        return 0
    minsteps = [0]*(n+1)
    minsteps[1]=0
    for currstep in range(2,n+1):
        subtract1 = minsteps[currstep-1]
        divby2 = MAX_VALUE
        divby3 = MAX_VALUE

        if currstep%2==0:
            divby2 = minsteps[currstep//2]

        if currstep%3==0:
            divby3 = minsteps[currstep//3]

        minsteps[currstep]=1+min(subtract1,divby2,divby3)
    return minsteps[n]
n = int(input())
print(countstepsto1(n))
