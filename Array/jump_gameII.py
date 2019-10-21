                                ###Jump Game II###
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""

class Solution(object):
    def jump(self, A):    
        min_d = 0
        last = 0       #keeps track of the maximum distance reached
        curr = 0 
        for i in range(0,len(A)):
            if i >  last:
                last = curr
                min_d = min_d + 1
            curr = max(curr, A[i]+i)
        return min_d    

