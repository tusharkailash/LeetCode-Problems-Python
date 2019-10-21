                                #First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}

        for i in s:
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1

        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1

s = "loveleetcode"
# s = "aabb"
# s  = "leetcode"
print Solution().firstUniqChar(s)