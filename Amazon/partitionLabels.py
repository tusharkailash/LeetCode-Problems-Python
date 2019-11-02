
# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

class Solution:
    def partitionLabels(self, S):
        lastIndex = {c: i for i, c in enumerate(S)}
        # print "lastIndex: ",lastIndex         #{'a': 8, 'c': 7, 'b': 5, 'e': 15, 'd': 14, 'g': 13, 'f': 11, 'i': 22, 'h': 19, 'k': 20, 'j': 23, 'l': 21}
        ans = []
        start = end = 0
        for i,c in enumerate(S):
            end = max(end, lastIndex[c])
            if i == end:
                ans.append(i - start + 1)
                start = i + 1

        return ans

S = "ababcbacadefegdehijhklij"
print Solution().partitionLabels(S)