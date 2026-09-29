class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        p = len(nums) - 2
        q = 1
        while goal > 0 and p >= 0:
            if nums[p] >= q:
                goal = p
                q = 1
            else:
                q += 1
            p -= 1

        return goal == 0
            


        