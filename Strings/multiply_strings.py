#Multiply Strings
#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#Note:
#1.	The length of both num1 and num2 is < 110.
#2.	Both num1 and num2 contains only digits 0-9.
#3.	Both num1 and num2 does not contain any leading zero.
#4.	You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        m = len(num1)
        n = len(num2)
        
        for i in range(m):
            a = int(num1[m-1-i])
            for j in range(n):
                b = int(num2[n-1-j])
                result = result + (a * b * (10 ** (i+j)))
                print result
				
num1= "34"
num2= "13"
ans = Solution().multiply(num1,num2)
print ans		
