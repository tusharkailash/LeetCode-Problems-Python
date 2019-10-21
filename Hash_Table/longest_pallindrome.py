                        ###Longest Palindrome

# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        res = 0

        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                                     # dict: {'a': 1, 'c': 5, 'b': 1, 'd': 2}
        for v in dict.values():
            res += v % 2
                                     # res = 1,1,2,2  i.e 2 is the no.
        if res >= 1:
            return len(s) - res + 1
        else:
            return len(s) - res

# Note: Reason for doing mod in "res += v % 2" : because we want to get the count of elements which will not be a part of the pallindrome.
# If res >= 1, it means that there is a possibility of adding a single element in the middle of the string to still form a pallindrome.
# If res <1 , ex: aabb, here res ==0, so output is just 4-0 = 4. i.e. there are no elements in the string with count = 1

s="acccccdd"
print Solution().longestPalindrome(s)