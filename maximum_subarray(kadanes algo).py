#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.

# nums = [-2,1,-3,4,-1,2,1,-5,4]
#output = 6
# largest sum= [4,-1,2,1]

def max_subarray(nums):
    curr = nums[0]
    head = nums[0]
    for i in range(len(nums)):
        curr = max(curr+nums[i],nums[i])
        head = max(head,curr)
    return head
