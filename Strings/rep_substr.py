#Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given #string consists of lowercase English letters only and its length will not exceed 10000.
#Example 1:
#Input: "abab"
#Output: True
#Explanation: It's the substring "ab" twice.

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type s: str
        :rtype: bool
        """
        if str == None:
           return False
        
        strLen = len(str)
        for i in range(strLen/2):
            substring = str[0:i+1]
            multiplier = strLen/(i+1)
            if str == substring*multiplier:
                return True
    
        return False
        
str="abab"
ans = Solution().repeatedSubstringPattern(str)
print ans		
