class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while abs(l-r) > 1:
            mid = l + (r-l)//2
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid

        return min(nums[l],nums[r])      