									###Search Insert Position###

#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.
#Here are few examples.
#[1,3,5,6], 5 → 2
#[1,3,5,6], 2 → 1
#[1,3,5,6], 7 → 4
#[1,3,5,6], 0 → 0

                
 class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n =len(nums)
        l = 0
        r =n-1
        while l<=r:
            mid = l + (r-l)/2
            
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                if mid == n-1:
                    return n
                if nums[mid+1]>target:
                    return mid+1
                else:
                    l = mid + 1
            else:
                if mid ==0:
                    return 0
                if nums[mid-1]<target:
                    return mid
                else:
                    r = mid -1
