
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        
        out = [False for i in range(n)]
        for i in range(n):
            if s[:i + 1] in wordDict:
                out[i] = True
            else:
                for j in range(i):
                    if out[j] is True and s[j + 1:i + 1] in wordDict:
                        out[i] = True

        return out[-1]

s = "leetcode"
wordDict = ["leet", "code"]
print Solution().wordBreak(s, wordDict)
