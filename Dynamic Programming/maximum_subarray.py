                        ###Maximum Subarray###

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        n = len(nums)
        if not nums or n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
            #print dp
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print Solution().maxSubArray(nums)
