				###Word Pattern###

#Examples:
#1.	pattern = "abba", str = "dog cat cat dog" should return true.
#2.	pattern = "abba", str = "dog cat cat fish" should return false.
#3.	pattern = "aaaa", str = "dog cat cat dog" should return false.
#4.	pattern = "abba", str = "dog dog dog dog" should return false.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()):
            return False
        d1 = {}
        d2 ={}
         
        for p,r in zip(pattern, str.split()):
            if p in d1:
                if d1[p] != r:
                    return False
            d1[p] = r
            if r in d2:
                if d2[r] != p:
                    return False
            d2[r] = p
        return True    
		
pattern = "abba"
str = "dog cat cat dog" 
ans = Solution().wordPattern(pattern,str)
print ans
