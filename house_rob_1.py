#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# nums = [1,2,3,1]
#output = 4

def house_rob(nums):
    n = len(nums)
    if not nums:
        return 0
    if n<=2:
        return max(nums)
    dp=[0]*n
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    return dp[n-1]
