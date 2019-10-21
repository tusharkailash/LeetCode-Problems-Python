                                ###Largest Number###
# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(num) for num in  nums]
        # print nums
        # nums= nums[::-1]
        # print ("Reverse : {}").format(nums)
        # print(arr)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) < (nums[j] + nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)


nums = [3, 30, 34, 5, 9]
print Solution().largestNumber(nums)
