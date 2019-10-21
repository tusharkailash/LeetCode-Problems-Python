                      ###Find All Numbers Disappeared in an Array###
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Example: Input: [4,3,2,7,8,2,3,1]
         Output: [5,6]                      
"""

class Solution():  
    def findDisappearedNumbers(self, nums):
        N = len(nums)
        for i in range(len(num  s)):
            x = nums[i] % N
            nums[x-1] += N
        return [i+1 for i in range(len(nums)) if nums[i]<=N]
   
   
nums = [4,3,2,7,8,2,3,1]
ans = Solution().findDisappearedNumbers(nums)
print (ans)
  


""" Iterations and the values obtained
i	          0	 1	 2	  3	  4	 5	6 	7
x	          4	 3	 2	  7	  0	 2	3	  1
nums[x-1]	  12 19	 18  15	  8	 2	11	9
"""
