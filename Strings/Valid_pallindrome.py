#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#For example,
#"A man, a plan, a canal: Panama" is a palindrome.
#"race a car" is not a palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        
        while l<r:
            while l<r and not s[l].isalnum():
                l = l+1
            while l<r and not s[r].isalnum():
                r = r-1
            if s[l].lower()!=s[r].lower():
                return False
            
            l = l + 1
            r = r - 1
        return True    
