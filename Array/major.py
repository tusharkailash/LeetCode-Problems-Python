#Majority element:
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example : nums = [4,1,4,4,2], return 4
"""


class Solution(object):
    def majorityElement(self, nums):
        
        count = 0 
        major = nums[0]
        for i in nums:
            if i == major:
                count = count+1
            else:
                count = count -1
            if count == 0:
                major = i
                count = 1    
        return major     


#Working:
#1st iteration: major = 4   (4==4)
#2nd iteration: major = 1   (1==4)
#3rd iteration: major = 4   (4==1)
#4th iteration: major = 4   (4==4)
#5th iteration: major = 4 and is returned.
