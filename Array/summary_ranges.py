"""Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []    
        start = end = nums[0]    
        
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                end = nums[i]
            else:
                res.append(self.getStr(start,end))
                start = end = nums[i]
        
        res.append(self.getStr(start,end))   
        
        return res
        
    def getStr(self,start,end):
        if start ==  end:
           return str(start)
        else:
           return str(start) + '->' + str(end)

