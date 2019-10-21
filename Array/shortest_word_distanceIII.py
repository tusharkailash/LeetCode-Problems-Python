                                ###Shortest Word Distance III###
"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.
Note:
You may assume word1 and word2 are both in the list.
"""                     

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        index1, index2 = size, size
        ans = size
        
        for i in xrange(size):
            if words[i] == word1:
                index1 = i
                ans = min(ans, abs(index1-index2))
                if word1==word2:
                   index2 = index1
            elif not (word1==word2) and words[i] == word2:
                index2 = i
                ans = min(ans, abs(index1-index2))
        return ans  

