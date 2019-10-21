#Example 1:
#Input: "USA"
#Output: True
#Example 2:
#Input: "FlaG"
#Output: False

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        lower = 0
        upper = 0
        for i in word:
            if i.isupper() and lower > 0:
                return False
            elif i.islower() and upper > 1:
                return False
            elif i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
        return True
