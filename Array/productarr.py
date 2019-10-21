                                           ###Product of array itself self####
"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product
of all the elements of nums except nums[i].
For example, given [1,2,3,4], return [24,12,8,6].
"""

class Solution(object):
    def productExceptSelf(self, nums):
        p=1
        output=[]
        n=len(nums)
        for i in range(0,n):
            output.append(p)
            p=p*nums[i]
        p=1
        for i in range(n-1,-1,-1):
            output[i]=output[i]*p
            p=p*nums[i]
        return output  

nums=[1,2,3,4]
ans = Solution().productExceptSelf(nums)
print ans
