#Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#https://www.youtube.com/watch?v=_Lf1looyJMU

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        squares = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        # print "squares:",squares
        largestSquare = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    squares[row+1][col+1]=0
                else:
                    squares[row + 1][col + 1] = min(squares[row][col],
                                                    squares[row+1][col],
                                                    squares[row][col+1]) + 1
                    largestSquare = max(largestSquare, squares[row + 1][col + 1])
        # print "largestSquare:",largestSquare
        return largestSquare*largestSquare

matrix = [
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]
print Solution().maximalSquare(matrix)