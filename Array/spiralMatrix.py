# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left = top = 0
        right = len(matrix[0]) - 1  # column
        bottom = len(matrix) - 1  # row

        result = []

        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])

            for i in range(top, bottom):
                result.append(matrix[i][right])

            for i in range(right, left, -1):
                result.append(matrix[bottom][i])

            for i in range(bottom, top, -1):
                result.append(matrix[i][left])

            left += 1
            top += 1

            right -= 1
            bottom -= 1

        if left == right and top == bottom:
            result.append(matrix[top][left])

        elif left == right:
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])

        elif top == bottom:
            for i in range(left, right + 1):
                result.append(matrix[bottom][i])

        return result

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print Solution().spiralOrder(matrix)