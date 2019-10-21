#You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
#Input: "1+1i", "1+1i"
#Output: "0+2i"
#Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
#Example 2:
#Input: "1+-1i", "1+-1i"
#Output: "0+-2i"
#Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i1, j1 = map(int, a[:-1].split("+"))
        i2, j2 = map(int, b[:-1].split("+"))
        result = str(i1*i2 - j1*j2) + "+" + str(i1*j2 + i2*j1) + "i"
        return result
