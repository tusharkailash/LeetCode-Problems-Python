						####Group Anagrams

#Given an array of strings, group anagrams together.
#For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
#Return:
#[
#  ["ate", "eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note: All inputs will be in lower-case.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anas = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s in anas:
               anas[s].append(string)
            else:
               anas[s] = [string]
        return [anas[i] for i in anas]
