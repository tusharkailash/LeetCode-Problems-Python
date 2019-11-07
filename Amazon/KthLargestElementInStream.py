# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
#
# Example:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8

import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val):
        if len(self.heap) == self.k:
            # This way we keep the k numbers of elements only and keep removing the smallest element
            # We maintain the k largest numbers by popping the smallest element
            heapq.heappushpop(self.heap, val)  #heappushpop pushes the val to heap and pops the min val from heap
        else:
            heapq.heappush(self.heap, val)      #when elements are pushed to heap, the order gets updated automatically

        return self.heap[0]


nums = [4,5,8,2]
obj = KthLargest(3, nums)
param_1 = obj.add(3)
param_1 = obj.add(5)
param_1 = obj.add(10)
param_1 = obj.add(9)
param_1 = obj.add(4)
param_1 = obj.add(11)
print param_1

