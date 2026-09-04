class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        options = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement in options:
                return [options[complement],i]
            options[num] = i

        return [-1,-1] # we assume the answer always exists