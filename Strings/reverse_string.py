							###Reverse String###

#Write a function that takes a string as input and returns the string reversed.
#Example:
#Given s = "hello", return "olleh".
#Subscribe to see which companies asked this question.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s) - 1
        s = list(s)
        
        while start <= end:
            s[start] , s[end] = s[end] , s[start]
            start += 1
            end -= 1
        
        return "".join(s)    
