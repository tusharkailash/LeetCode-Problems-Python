# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
# 
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):

        rowLength = len(image)
        colLength = len(image[0])
        color = image[sr][sc]
        stack = [(sr, sc)]
        visited = {(sr, sc)}

        while stack:
            r, c = stack.pop()
            if 0 <= r < rowLength and 0 <= c < colLength and image[r][c] == color:
                image[r][c] = newColor
                if (r - 1, c) not in visited:
                    stack.append((r - 1, c))
                    visited.add((r - 1, c))
                if (r + 1, c) not in visited:
                    stack.append((r + 1, c))
                    visited.add((r + 1, c))
                if (r, c - 1) not in visited:
                    stack.append((r, c - 1))
                    visited.add((r, c - 1))
                if (r, c + 1) not in visited:
                    stack.append((r, c + 1))
                    visited.add((r, c + 1))
        return image


image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
newColor = 2
print Solution().floodFill(image,sr,sc,newColor)