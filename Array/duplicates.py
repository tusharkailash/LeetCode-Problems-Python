# -Remove-Duplicates-from-Sorted-Array-

"""For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length."""



class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        newTail = 0
        for i in range(1,len(nums)):
              if nums[i] != nums[newTail]:
                   newTail = newTail + 1
                    nums[newTail] = nums[i]
        return newTail + 1    

    
nums = [1,2,3,3,4,6,7]
ans = Solution().removeDuplicates(nums)
print ans
