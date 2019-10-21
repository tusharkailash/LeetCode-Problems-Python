                                          ###Rotate Array

# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].


class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        return nums

    def reverse(self, nums, start, end):
        while (start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1


nums = [1,2,3,4,5,6,7]
k = 4
print Solution().rotate(nums,k)