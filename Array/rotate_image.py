                                  ###Rotate Image###
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = len(matrix)-1
        for i in range(n//2 + 1):
            for j in range(i,n-i):
                temp = matrix[i][j]
                matrix[i][j]=matrix[n-j][i]
                matrix[n-j][i]=matrix[n-i][n-j]
                matrix[n-i][n-j]=matrix[j][n-i]
                matrix[j][n-i]=temp
        return matrix
         
		
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans= Solution().rotate(matrix)
print ans	

