                                #Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        ds = {}
        dp = {}

        ls = len(s)
        lp = len(p)

        res = []

        for i in s[:lp]:  # iterating over the len of p
            ds[i] = ds.get(i, 0) + 1
        for i in p[:lp]:
            dp[i] = dp.get(i, 0) + 1

        i = 0
        while i < (ls - lp):

            if ds == dp:  # here if the ds and dp have the same elements , append the index
                res.append(i)

            ds[s[i]] -= 1  # remove the first index in order to add the 4th and check the same process

            if ds[s[i]] == 0:  # if the value of an element decremented is not 0, keep it.
                del ds[s[i]]

            if s[i + lp] in ds:  # adding the 4th element, i.e s[i+lp]  "i+ lp" will take iver to the next element
                ds[s[i + lp]] += 1
            else:
                ds[s[i + lp]] = 1

            i += 1  # increment the value of i and repeat

        if ds == dp:  # for the last position
            res.append(i)
        return res


s =  "cbaebabacd"
p = "abc"
print Solution().findAnagrams(s,p)