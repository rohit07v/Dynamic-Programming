import sys

def eggdrop_recursion(e, f):
    if f == 1 or f == 0:
        return f

    if e == 1:
        return f

    min = sys.maxsize

    for x in range(1, f + 1):
        res = max(eggdrop(e - 1, x - 1),
                  eggdrop(e, f - x))
        if res < min:
            min = res

    return min + 1



def eggdrop_dp(e, f):
    if f == 1 or f == 0:
        return f

    if e == 1:
        return f
    dp=[[-1 for i in range(f+1)]for j in range(e+1)]
    min = sys.maxsize
    if dp[e][f]!=-1:
        return dp[e][f]

    for x in range(1, f + 1):
        res = 1+max(eggdrop(e - 1, x - 1),
                  eggdrop(e, f - x))
        if res < min:
            min = res
    dp[e][f]=min
    return min

e=2
f=10

print(eggdrop_dp(e,f))
