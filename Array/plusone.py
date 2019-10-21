
############PLUS ONE###


"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range (len(digits)):
            num = num + (digits[i] * pow(10,digits[i]-1-i))
        new_num = num + 1	
        return [int(i) for i in str(new_num)]
		
digits = [3,2,4,5]	
ans = Solution().plusOne(digits)
print ans
