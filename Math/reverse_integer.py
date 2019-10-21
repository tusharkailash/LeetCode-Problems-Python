                                    ####Reverse Integer####


# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
#[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        if x < 0:
            sym = -1
            x = -x  # making the number as positive
        else:
            sym = 1

        while x:
            res = (res * 10) + (x % 10)
            x = x / 10
            # Number is reversed

        #check for overflow

        if res < pow(2, 31):
            return res * sym
        else:
            return 0


x = -123
print Solution().reverse(x)