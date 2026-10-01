"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        heap = []

        sort = sorted(intervals, key=lambda x:x.start)

        for interval in sort:
            if heap and interval.start >= heap[0]:
                heappop(heap)

            heappush(heap,interval.end)

        return len(heap)

        