#Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k #characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other #as original.
#Example:
#Input: s = "abcdefg", k = 2
#Output: "bacdfeg"
#Restrictions:
#1.	The string consists of lower English letters only.
#2.	Length of the given string and k will in the range [1, 10000]


			###Best Solution:

# class Solution(object):
#     def reverseStr(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         s = list(s)
#         for i in range(0, len(s), 2*k):    #left
#             j = min(i+k-1,len(s)-1)                              #no need to actually use min. just writing i+k-1 works too
#             while i < j:                   #right
#                 s[i] , s[j] = s[j] , s[i]
#                 i += 1
#                 j -= 1
#         return "".join(s)
                   
###second solution:

# class Solution(object):
#     def reverseStr(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         s = list(s)
#         for i in range(0,len(s),2*k):
#             s[i:i+k]=reversed(s[i:i+k])
#         return "".join(s)
#


###Solution:

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
            print s
        # return "".join(s)


s = "abcdefghij"
k=2
ans= Solution().reverseStr(s,k)
print ans		
