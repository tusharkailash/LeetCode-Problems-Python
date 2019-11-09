# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island_count += 1
                    self.changeLandToWater(grid, i, j)

        return island_count

    def changeLandToWater(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.changeLandToWater(grid, i - 1, j)  # down
        self.changeLandToWater(grid, i + 1, j)  # up
        self.changeLandToWater(grid, i, j - 1)  # left
        self.changeLandToWater(grid, i, j + 1)  # right


grid = [
  ['1',   '1',  '0',  '1', '1'],
  ['1',   '0',  '0',  '0', '0'],
  ['0',   '0',  '1',  '0', '0'],
  ['0',   '0',  '0',  '0', '1'],
  ['1',   '1',  '0',  '1', '1'],
]

print Solution().numDistinctIslands(grid)





