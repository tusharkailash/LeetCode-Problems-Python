#Write a function that takes a string as input and reverse only the vowels of a string.
#Example 1:
#Given s = "hello", return "holle".
#Example 2:
#Given s = "leetcode", return "leotcede".
#Note:

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while j > i and L[j] not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i] 
            i += 1
            j -= 1
        return ''.join(L)
 
s="hello"
ans = Solution().reverseVowels(s)
print ans
