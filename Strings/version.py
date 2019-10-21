"""Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 13.37
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1 = version1.split(".")
        list2 = version2.split(".")
        maxlen = max(len(list1),len(list2))
        
        for i in range(maxlen):
            if i < len(list1):
                v1 = int(list1[i])
            else:
                v1 = 0
            if i < len(list2):
                v2 = int(list2[i])
            else:
                v2 = 0    
            
            if v1>v2:
                return 1
            elif v1<v2:
                return -1
        return 0        
                
