# Missing Number
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example,
Given nums = [0, 1, 3] return 2.
"""


class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)       #sum(0+1+2+3)-sum(0+1+3) = 2
    
nums = [0,1,2,3]
ans = Solution().missingNumber(nums)
print (ans)

