                            #####Sort Colors######

###Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1  # because 1 is the fixed pole. no changes to it. 0 to its left and 2 to its right

            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1  # not decrementing mid as the mid swapped can be 0 to, so we need to check that case
        return nums

        ###SOLUTION 2


        # i = 0
        # k = 0
        # for j in range(len(nums)):
        #     if nums[j] == 0:
        #         temp = nums[i]
        #         nums[i] = nums[j]
        #         nums[j] = temp
        #         i += 1
        # k = i
        # # print nums
        # # print k
        # for j in range(k, len(nums)):
        #     if nums[j] == 1:
        #         temp = nums[k]
        #         nums[k] = nums[j]
        #         nums[j] = temp
        #         k += 1

#
# nums = [0,2,1,2,0]
nums = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print Solution().sortColors(nums)