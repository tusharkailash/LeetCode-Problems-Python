# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Example 1:
#
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

class Solution(object):
    def lastStoneWeight(self, stones):

        while (len(stones) > 1):
            stones.sort(reverse=True)
            i = stones.pop(0)
            j = stones.pop(0)
            if (i != j):
                stones.append(abs(i - j))
        if len(stones) == 0:                 #For ex: check with input as [2,2]
            return 0
        return stones[0]


stones = [2,7,4,1,8,1]
# stones = [2,2]
print Solution().lastStoneWeight(stones)