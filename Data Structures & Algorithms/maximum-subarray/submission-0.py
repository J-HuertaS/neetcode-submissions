class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = float('-inf')
        currSum = 0
        for i in range(len(nums)):
            currSum = nums[i] if currSum < 0 else currSum + nums[i]
            output = max(output,currSum)

        return output