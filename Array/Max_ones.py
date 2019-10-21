						###Maximum Consecutive Ones###
				
#Input: [1,1,0,1,1,1]                 i/p consists of 0 and 1 only.
#Output: 3 

class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        ans=0
        count = 0
        for n in nums:
            if n == 1:
                count = count + 1
                ans = max(ans, count)
            else:
                count = 0
        return ans
   
nums = [1,1,1,1,0,1,1,1]
out = Solution().findMaxConsecutiveOnes(nums)
print (out)
