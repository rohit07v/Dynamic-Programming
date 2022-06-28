#Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

#The test cases are generated so that the answer will fit in a 32-bit integer.

#A subarray is a contiguous subsequence of the array.

#nums = [2,3,-2,4]
#output = 6


def maxProduct(nums):
    mini = 1
    maxi = 1
    res = max(nums)
    for i in nums:
        if i==0:
            mini,maxi =1,1
            continue
        temp = maxi*i
        maxi = max(maxi*i,mini*i,i)
        mini = min(maxi*i,temp,i)
        res = max(maxi,mini,res)
    return res
