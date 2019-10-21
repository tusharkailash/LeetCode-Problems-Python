#Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#Please note that the string does not contain any non-printable characters.
#Example:
#Input: "Hello, my name is John"
#Output: 5

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        return len(s)	

Appropriate solution:
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count  = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i==0 or s[i-1]==' '):
                count += 1
        return count        

