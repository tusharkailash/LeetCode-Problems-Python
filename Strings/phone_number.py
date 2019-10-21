#Input:Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
         if not digits:
            return []
         dict= {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
         result =[""]
         for i in digits:
             newresult=[]
             lst =dict[i]
             for char in lst:
                 for j in result:
                     newresult.append(j+char)
             result = newresult     
         return result
