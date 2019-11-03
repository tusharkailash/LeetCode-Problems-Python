# There are 8 prison cells in a row, and each cell is either occupied or vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the following rules:
#
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
#
# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
#
# Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
# Example 1:
#
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

class Solution(object):
    def prisonAfterNDays(self, cells, N):

        def nextday(cells):
            next_day_cells = [0] *len(cells)
            for i in range(1,len(cells)-1):
                if cells[i-1] == cells[i+1]:
                        next_day_cells[i] = 1
                else:
                        next_day_cells[i] = 0
            return tuple(next_day_cells)

        seen = {}

        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N
            # print "c :",c
            # print "seen : ",seen
            # print "-"*100

            if N >= 1:
                N -= 1
                cells = nextday(cells)
        return cells


cells = [0,1,0,1,1,0,0,1]
N = 7
print Solution().prisonAfterNDays(cells,N)


# N = N%(seen(c)-N)
# The trick point here is that this algorithm starts to label the pattern at N.
# Let's say N = 30. we calculate 14 times nextday then we find a pattern. However, the pattern starts at N.
# The pattern stores in the seen would be: I put 0-14 index after it.
# seen={
# (0, 1, 0, 1, 1, 0, 0, 1): 30, 0
# (0, 1, 1, 0, 0, 0, 0, 0): 29, 1
# (0, 0, 0, 0, 1, 1, 1, 0): 28, 2
# (0, 1, 1, 0, 0, 1, 0, 0): 27, 3
# (0, 0, 0, 0, 0, 1, 0, 0): 26, 4
# (0, 1, 1, 1, 0, 1, 0, 0): 25, 5
# (0, 0, 1, 0, 1, 1, 0, 0): 24, 6
# (0, 0, 1, 1, 0, 0, 0, 0): 23, 7
# (0, 0, 0, 0, 0, 1, 1, 0): 22, 8
# (0, 1, 1, 1, 0, 0, 0, 0): 21, 9
# (0, 0, 1, 0, 0, 1, 1, 0): 20, 10
# (0, 0, 1, 0, 0, 0, 0, 0): 19, 11
# (0, 0, 1, 0, 1, 1, 1, 0): 18, 12
# (0, 0, 1, 1, 0, 1, 0, 0): 17, 13
# (0, 0, 0, 0, 1, 1, 0, 0): 16} 14
#
# when N =15 (15), we know it happened at N=29 (1)
# N = (15%(29-15)) =1
# update seen[(0, 1, 1, 0, 0, 0, 0, 0)= 1(used to be 29)
# N>=1:
# N = 1 -1 = 0
# cells = nextday((0, 1, 1, 0, 0, 0, 0, 0))
# N = 0, the while loop will end.

# With the aboe input it doesnt enter the if statment "if c in seen"