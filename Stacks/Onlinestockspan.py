                    ####      Stock Span Problem    ####

# Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
# The span of the stock's price today is defined as the maximum number of consecutive
# days (starting from today and going backwards) for which the price of the stock was less
# than or equal to today's price.

# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60,75, 85],
# then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

                    #Solution1 : O(n2)

class Solution(object):
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        S = [None] * len(price)
        S[0] = 1


        for i in range(1, len(price)):
            S[i] = 1  # Initialize span value

            j = i - 1
            while (j >= 0) and (price[i] >= price[j]):
                S[i] += 1
                j -= 1
        return S

price = [10, 4, 5, 90, 6, 3, 120, 80]
print Solution().next(price)


Solution2 : O(n)

class Solution():
    def calculateSpan(self,price):

        S = [0] * len(price)
        S[0] = 1                 # Span value of first day is always 1

        st = []
        st.append(0)

        for i in range(1, len(price)):

            # Pop elements from stack while stack is not
            # empty and top of stack is smaller than price[i]
            while (len(st) > 0 and price[st[-1]] <= price[i]):
                st.pop()
            #If stack becomes empty, then price[i] is greater
            # than all elements on left of it, i.e. price[0],
            # price[1], ..price[i-1]. Else the price[i] is
            # greater than elements after top of stack
            S[i] = i + 1 if len(st) <= 0 else (i - st[-1])

            # Push this element to stack
            st.append(i)
        print S

price = [10, 4, 5, 90, 6, 3, 120, 80]
print Solution().calculateSpan(price)

