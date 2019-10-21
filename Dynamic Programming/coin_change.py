                                    ###Coin Change###

# You are given coins of different denominations and a total amount of money amount.
#  Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [amount+1] * (amount+1)                # [12,12,12,12,12,12,12,12,12,12,12,12]
        res[0] = 0                                   # [0,12,12,12,12,12,12,12,12,12,12,12]
        for i in xrange(1, amount+1):
            for c in coins:
                if i >= c:
                    res[i] = min(res[i], res[i-c] + 1)

        if res[amount] == amount+1:
            return -1                                # In this case it is false
        else:
            return res[amount]


coins = [1,2,5]
amount = 11
print Solution().coinChange(coins,amount)
