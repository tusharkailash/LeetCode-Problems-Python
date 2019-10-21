							###Palindrome Permutation###

#Given a string, determine if a permutation of the string could form a palindrome.
#For example,
#"code" -> False, "aab" -> True, "carerac" -> True.

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {}
        for item in s:
            dict[item] = dict.get(item,0)+1
        count = 0
        for i in dict.values():
            if i % 2  == 1:
               count += 1
            if count > 1:
               return False    
        return True       

