# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):

        startintervals = sorted(intervals)          #sort intervals according to their start times
        heap = []
        for interval in startintervals:
            if not heap:
                heapq.heappush(heap, interval[1])
                # print heap
            else:
                start, end  = interval[0],interval[1]
                if start >= heap[0]:        # = if the meeting starts on the same time as end of prev meeting
                    heapq.heappop(heap)     # pop the prev end time as the same meeting room can be used and update with the new end time
                heapq.heappush(heap, end)
        return len(heap)

intervals = [[0, 30], [5, 10], [15, 20]]
# intervals = [[7,10],[2,4]]
print Solution().minMeetingRooms(intervals)
