                                ###Third Maximum Number

# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = None, None, None
        for i in nums:
            if i > first:
                third = second
                second = first
                first = i
            elif i > second and i != first:
                third = second
                second = i
            elif i > third and i != second and i != first:
                third = i
        return first if third is None else third


nums = [2,2,5,8]
print Solution().thirdMax(nums)
