#You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

#Return true if you can reach the last index, or false otherwise.

#nums=[2,3,1,1,4]
#output = True



def jump_game_method1(nums):
    start = 0
    last = len(nums)-1
    for i in range(len(nums)):
        if i>start:
            return False
        if nums[i]+i>start:
            start = nums[i]+i
        if start>=last:
            return True


def jump_game_method2(nums):
    size = len(nums)
    dp = [0]*(size)
    if len(nums)<2:
        return True
    dp[0]=nums[0]
    for i in range(1,size):
        if dp[i-1]==0:
            return False
        dp[i]=max(dp[i-1]-1,nums[i])
    return True
