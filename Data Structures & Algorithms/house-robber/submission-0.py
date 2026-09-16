class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]


        output = [0 for _ in range(len(nums)+1)]

        output[1] = nums[0]

        for i in range(2,len(output)):
            temp = max(output[i-1],output[i-2]+nums[i-1])
            output[i] = temp

        return output[len(nums)]


        