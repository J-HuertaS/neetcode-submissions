class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        goal = n * (n + 1) // 2

        goal -= sum(nums)
            
        return goal
        