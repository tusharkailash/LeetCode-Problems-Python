
#Given an input string, reverse the string word by word.
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i =0
        result=""
        for j in range(len(s) + 1):
            if j==len(s) or s[j]==' ':
                 if i!=j:
                     result = s[i:j] + ' ' + result
                 i = j + 1
        return result.strip()         
             
        
s = "the sky is blue "
ans = Solution().reverseWords(s)
print ans
