#Input: "abab"
#Output: True
#Explanation: It's the substring "ab" twice.
#Example 2:
#Input: "aba"
#Output: False
#Example 3:
#Input: "abcabcabcabc"
#Output: True
#Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        ss= (s+s)[1:-1]
        if s in ss:
            return True
        else:
            return False
