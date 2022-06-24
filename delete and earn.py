#You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

#Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

#Return the maximum number of points you can earn by applying the above operation some number of times.

# nums = [3,4,2]
#output = 6



def delete_and_earn(nums):
    n = len(nums)
    dp=[0]*(max(nums)+1)
    for i in nums:
        dp[i]+=i
    for i in range(2,len(dp)):
        dp[i]=max(dp[i-1],dp[i-2],dp[i])
    return dp[-1]
        
