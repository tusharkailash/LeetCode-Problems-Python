							###Integer to Roman###    

#Given an integer, convert it to a roman numeral.
#Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return a string
    def intToRoman(self, num):
        roman = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 
                  40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        result  = ""
        for i in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
            result = result + roman[i] * (num//i)
            num= num % i
        return result    
