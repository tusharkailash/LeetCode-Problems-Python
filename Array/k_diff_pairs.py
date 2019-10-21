                                                 ###K-diff Pairs in an Array###


"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
"""

class Solution:
    def findPairs(self, nums, k):
        if k>0:
            return len(set(nums)&set(n + k for n in nums))
        elif k==0:
            return sum(i>1 for i in collections.Counter(nums).values())
        else:
            return 0
