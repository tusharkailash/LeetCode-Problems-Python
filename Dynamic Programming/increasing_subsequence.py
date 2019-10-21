                                    ###Longest Increasing Subsequence###

# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.



class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dp = [1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1

        #print out the laregest number from the array
        lar = 0
        for i in range(n):
            lar = max(lar , dp[i])
        return lar



nums = [3,4,-1,0,6,2,3]
print Solution().lengthOfLIS(nums)
