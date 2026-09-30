class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        p = 1

        while p < len(intervals):
            start = intervals[p][0]
            end = intervals[p][1]
            if prev_start <= start <= prev_end or prev_start <= end <= prev_end:
                prev_start = min(prev_start,start)
                prev_end = max(prev_end,end)
            else:
                res.append([prev_start,prev_end])
                prev_start = start
                prev_end = end

            p += 1

        res.append([prev_start,prev_end])

        return res
                

            

            

        