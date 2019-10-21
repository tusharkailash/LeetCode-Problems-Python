						###Valid Anagram###

#Given two strings s and t, write a function to determine if t is an anagram of s.
#For example,
#s = "anagram", t = "nagaram", return true.
#s = "rat", t = "car", return false.
#Note:
#You may assume the string contains only lowercase alphabets.

#http://stackoverflow.com/questions/2068349/understanding-get-method-in-python

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
        for i in s:
            dict1[i] = dict1.get(i,0) + 1
        for j in t:
            dict2[j] = dict2.get(j,0) + 1
        if dict1 == dict2:
            return True
        else:
            return False

