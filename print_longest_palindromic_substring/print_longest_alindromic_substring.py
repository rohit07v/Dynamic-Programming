def is_pal(s,left,right):
    while left>=0 and right<len(string) and string[left]==string[right]:
        left-=1
        right+=1
    return string[left+1:right]


def lps(string):
    res=""
    for i in range(len(string)):
        odd = is_pal(string,i,i)
        even = is_pal(string,i,i+1)
        res = max(res,odd,even,key = len)
    return res


string = "cbbd"
print(lps(string))
