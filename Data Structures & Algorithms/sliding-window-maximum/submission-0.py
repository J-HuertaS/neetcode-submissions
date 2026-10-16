from heapq import heappop, heappush, heapify

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        heapify(h)

        output = []

        p = 0

        while p < k:
            heappush(h,(-nums[p],p))
            p += 1
            
        output.append(h[0][0]*-1)

        while p < len(nums):
            heappush(h,(-nums[p],p))
            
            while p-k >= h[0][1] or h[0][1] > p:
                heappop(h)
            output.append(h[0][0]*-1)
            
            p += 1

        return output

            
        