#Rotate array

"""
Rotate an array of n elements to the right by k steps. 
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""


class Solution(object):
    def rotate(self, nums, k):	
        k = k%len(nums)
        nums[:] = nums[-k:]+nums[:-k]
	return nums

nums = [4,3,2,7,8,2,3,1]
ans = Solution().rotate(nums,3)
print ans

       
# nums[:] is equivalent of nums. This will have the numbers included from start to end.
# nums[-k:] is the partial array of the last k items. = [5,6,7]
# nums[:-k] is the partial array from first element to nums[len(nums)-k] = [1,2,3,4]
