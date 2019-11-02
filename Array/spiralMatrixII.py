# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left = top = 0
        right = n - 1
        bottom = n - 1

        num = 1

        matrix = [[0 for i in range(n)] for i in range(n)]

        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = num
                num += 1

            for i in range(top, bottom):
                matrix[i][right] = num
                num += 1

            for i in range(right, left, -1):
                matrix[bottom][i] = num
                num += 1

            for i in range(bottom, top, -1):
                matrix[i][left] = num
                num += 1

            left += 1
            top += 1
            right -= 1
            bottom -= 1

        if left == right and top == bottom:
            matrix[top][left] = num

        return matrix

n = 3
print Solution().generateMatrix(n)