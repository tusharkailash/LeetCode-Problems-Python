# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]

class Solution(object):
    def topKFrequent(self, nums, k):

        dict = {}
        output = []
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        # print dict.items()
        sortedNums = sorted(dict.items(), key = lambda k: k[1], reverse = True)

        for i in range(k):
            output.append(sortedNums[i][0])
        return output

nums = [1,1,1,2,2,3,5,5,5,5,5]
k = 2
print Solution().topKFrequent(nums,k)