class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        dict1 = {}
        dict2 = {}

        if len(ransomNote) > len(magazine):
            return False

        for i in ransomNote:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for j in magazine:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1

        # print 'dict1 =',dict1, 'dict2=',dict2

        for i in dict1:
            if i not in dict2 or dict2[i] < dict1[i]:
                return False
        return True

ransomNote = "aa"
magazine = "ab"
print Solution().canConstruct(ransomNote,magazine)