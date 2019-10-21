                            ###Remove Element###

"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        start = 0
        last = len(A)-1
        while start <= last:
            if A[start] == elem:
                if A[last] == elem:
                    last -= 1
                else:
                    A[start] = A[last]
                    last -= 1
                    start += 1
            else:
                start += 1
        return start 









