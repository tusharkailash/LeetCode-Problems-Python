								###KEYBOARD ROW###

#Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image 
#Input: ["Hello", "Alaska", "Dad", "Peace"]
#Output: ["Alaska", "Dad"]

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        out = []       #list
        for i in words:
            w = set(i.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
               out.append(i)
        return out
