                                ####Merge Sorted Array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.



class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return

        idx = m + n - 1
        i = m - 1
        j = n - 1

        while idx >= 0 and i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1

        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]

        return nums1
nums1 = [1,5,7]
nums2 = [2,3,4]
m = 2
n = 1
print Solution().merge(nums1,m,nums2,n)
