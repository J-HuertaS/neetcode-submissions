class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSub = nums[0]
        minSub = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == 0:
                maxSub = 0
                minSub = 0
            else:
                tempSub = max(maxSub*nums[i],nums[i],minSub*nums[i])
                minSub = min(nums[i],minSub*nums[i],maxSub*nums[i])
                maxSub = tempSub
            result = max(result,maxSub)

        return result

            

        