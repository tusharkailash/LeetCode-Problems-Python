#For example, Given s = "Hello World",return 5.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        n = len(s)
        num = 0
        for i in reversed(range(n)):
            if (s[i] == ' '):
                break
            num = num + 1
        
        return num    
		
s = "Hello World"
ans = Solution().lengthOfLastWord(s)
print ans	



###Optimal Solution###

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in xrange(len(s)-1, -1, -1):
            if s[i] != ' ':
                ans += 1
            elif ans:
                break
        return ans
