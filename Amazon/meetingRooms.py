# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
#
# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: true

class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort()
        # print intervals
        for i in range(len(intervals) - 1):
            if intervals[i][-1] > intervals[i + 1][0]:
                return False
        return True

intervals = [[0,30],[5,10],[15,20]]
# intervals = [[7,10],[2,4]]
print Solution().canAttendMeetings(intervals)
