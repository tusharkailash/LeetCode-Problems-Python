								###Strobogrammatic Number###
								
#A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#For example, the numbers "69", "88", and "818" are all strobogrammatic.

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict = {'8':'8','1':'1','0':'0','6':'9','9':'6'}
        l = 0
        r = len(num)-1
        while l<=r:
            if num[l] not in dict or dict[num[l]]!=num[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        
