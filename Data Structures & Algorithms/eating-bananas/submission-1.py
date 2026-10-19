import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = (r-l)//2 + l
            horas_usadas = sum(math.ceil(p / mid) for p in piles)
            if horas_usadas <= h:
                r = mid
            else:
                l = mid + 1

        return l

        

        