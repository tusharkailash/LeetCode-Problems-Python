							###Single Number I###

#Given an array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#[1,2,3,3,2,5]   output = 5

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
        
            dict[i] = dict.get(i,0) + 1
        #print dict
        for key,val in dict.items():
            if val == 1:
                return key
