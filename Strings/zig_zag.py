								###ZigZag Conversion###

#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better #legibility)
#		P   A   H   N
#		A P L S I I G
#		Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR" .Write the code that will take a string and make this conversion given a number of rows:
#string convert(string text, int nRows);
#convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        temp = ['' for i in range(numRows)]
        if numRows == 1:
            return s
        index = 1
        step = -1
        for i in range(len(s)):
            index = index + step
            
            if index == numRows:
               index = index - 2
               step = -1
            elif index == -1:
                index = 1 
                step = 1
            temp[index] = temp[index] + s[i]
        return ''.join(temp)        

['P', '', '']
['P', 'A', '']
['P', 'A', 'Y']
['P', 'AP', 'Y']
['PA', 'AP', 'Y']
['PA', 'APL', 'Y']
['PA', 'APL', 'YI']
['PA', 'APLS', 'YI']
['PAH', 'APLS', 'YI']
['PAH', 'APLSI', 'YI']
['PAH', 'APLSI', 'YIR']
['PAH', 'APLSII', 'YIR']
['PAHN', 'APLSII', 'YIR']
['PAHN', 'APLSIIG', 'YIR']
