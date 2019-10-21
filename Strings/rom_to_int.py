						###Roman to Integer###

#Given a roman numeral, convert it to an integer.
#Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = dict[s[-1]]                     #result in last element. Ex: XCIX : result = 10
        
        for i in range(len(s)-2,-1,-1):   #going in reverse direction. In this case from I to X
            if dict[s[i]] < dict[s[i+1]]:
               result -= dict[s[i]]
            else:
               result += dict[s[i]]
        return result
