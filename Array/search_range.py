                            ###Search for a Range###

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                ans.append(i)
                break

        return ans if ans else [-1, -1]


nums = [5,7,7,8,8,10]
target = 8
print Solution().searchRange(nums,target)