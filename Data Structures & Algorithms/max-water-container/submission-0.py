class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        output = 0

        while(l < r):
            area = min(height[l],height[r]) * (r-l)
            output = max(output,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return output