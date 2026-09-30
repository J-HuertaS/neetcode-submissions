class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sort = sorted(intervals, key=lambda x: (x[0],-x[1]-x[0]))
        # si el anterior se solapa, lo cuento como eliminacion y utilizo el greedy approach de mantener el prev_end minimo que abarca menos distancia
        prev_end = sort[0][1]
        p = 1
        ans = 0

        while p < len(sort):
            if sort[p][0] < prev_end:
                ans += 1
                prev_end = min(prev_end,sort[p][1])
            else:
                prev_end = sort[p][1]

            p += 1

        return ans
        