# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
# Words in the list of banned words are given in lowercase, and free of punctuation.
# Words in the paragraph are not case sensitive.  The answer is in lowercase.


# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        p = ["!","?","'",",",";","."]
        dict = {}

        for i in paragraph:
            if i in p:
                paragraph = paragraph.replace(i, ' ')

        paragraph = paragraph.lower().split()

        for i in paragraph:
            if i in banned:
                continue
            elif i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        maximum = max(dict.values())

        for i in dict:
            if dict[i] == maximum:
                return i



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print Solution().mostCommonWord(paragraph,banned)