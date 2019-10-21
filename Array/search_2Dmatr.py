                                     ###Search a 2D Matrix###

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
•	Integers in each row are sorted from left to right.
•	The first integer of each row is greater than the last integer of the previous row.
For example,
Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mid = l + (r-l)/2
            elem = matrix[mid/n][mid%n]
            if elem == target:
                return True
            elif elem <target:
                l = mid + 1
            else:
                r = mid - 1
        return False    
    
		
matrix = [[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
ans= Solution().searchMatrix(matrix,3)
print ans		

