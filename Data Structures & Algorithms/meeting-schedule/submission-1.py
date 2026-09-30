"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True 
            
        sort = sorted(intervals, key=lambda x:x.start)
        prev_end = sort[0].end
        p = 1
        while p < len(sort):
            if sort[p].start < prev_end:
                return False
            prev_end = sort[p].end
            p += 1

        return True
