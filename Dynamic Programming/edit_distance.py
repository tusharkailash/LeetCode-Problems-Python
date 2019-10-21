                                            ###Edit Distance###

# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):

        dp = [[0 for x in range(len(word2)+1)] for x in range(len(word1)+1)]

        # Fill d[][] in bottom up manner
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):

                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                       dp[i-1][j],        # Remove
                                       dp[i-1][j-1])    # Replace
                #print dp
        return dp[len(word1)][len(word2)]

word1 = "cart"
word2 = "march"
print Solution().minDistance(word1,word2)
