                                ###Longest Harmonious Subsequence

# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                # {1: 1, 2: 3, 3: 2, 5: 1, 7: 1}
        ans = 0

        # Iterate over the dict and check if for the element, there exists a next element. If it exists, add the current and next element value. Here, in the above example, we will add the values of {1: 1, 2: 3, 3: 2} in the code below.

        for i in dict:
            if dict.get(i + 1):
                ans = max(ans, dict[i] + dict[i + 1])

        return ans

# mp.get(i+1)
# 3
# mp[i],mp[i+1]
# 1 3
# ln
# 4
# -----
# mp.get(i+1)
# 2
# mp[i],mp[i+1]
# 3 2
# ln
# 5
# -----
# 5     = ans


nums = [1,3,2,2,5,2,3,7]
print Solution().findLHS(nums)