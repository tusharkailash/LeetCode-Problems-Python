                                            ###Subset Sum Problem###

# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
#
# Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.

class Solution():
    def subset_sum(self,nums,sums):

        m = len(nums)
        dp = [[False for i in range(sums+1)] for i in range(m+1)]

        for i in range(m):
            dp[i][0] = True
        #print dp

        for i in range(1,m+1):
            for j in range(1,sums+1):
                if (j - nums[i - 1] >= 0):
                    dp[i][j] = (dp[i - 1][j]) or (dp[i - 1][j - nums[i - 1]])
                else:
                    dp[i][j] = dp[i-1][j]


        return dp[m][sums]



nums = [2, 3, 7, 8, 10]
sums = 11
print Solution().subset_sum(nums,sums)
