                                        #ISOMORPHIC STRINGS

# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
#  No two characters may map to the same character but a character may map to itself.
# For example,
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.
# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in dict1 and dict1[s[i]] != t[i]:
                return False
            else:
                dict1[s[i]] = t[i]

        for i in range(len(t)):
            if t[i] in dict2 and dict2[t[i]] != s[i]:
                return False
            else:
                dict2[t[i]] = s[i]

        return True


s = "ab"
t = "ca"
print Solution().isIsomorphic(s,t)

# Note: The two for loops and dictionary are needed in order to check the mappings (for output ab and ca)