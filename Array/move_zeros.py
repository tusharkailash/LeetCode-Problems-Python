                        ###Move Zeros###
""""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""
                
 class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        zero = 0  # records the position of "0"
        for i in xrange(len(nums))003A
            if nums[i] != 0:
               nums[i], nums[zero] = nums[zero], nums[i]
               zero += 1
	return nums	



nums=[1,0,5,0,0,4]
ans = Solution().moveZeroes(nums)
print ans	
	
