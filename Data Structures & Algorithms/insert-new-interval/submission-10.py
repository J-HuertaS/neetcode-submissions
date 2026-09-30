class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1

        start_i = i

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i += 1

        intervals[start_i:i] = [newInterval]

        return intervals

        
        