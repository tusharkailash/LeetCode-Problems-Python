                        ###Longest Common Subsequence###

# Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences between two files), and has applications in bioinformatics.
#
# Examples:
# LCS for input Sequences ABCDGH and AEDFHR is ADH of length 3.
# LCS for input Sequences AGGTAB and GXTXAYB is GTAB of length 4.


class Solution(object):
    def longest_common_subq(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0 for i in range(n+1)] for i in xrange(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]

str1 = "abcdaf"
str2 = "acbcf"
print Solution().longest_common_subq(str1,str2)
