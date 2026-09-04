class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        output = []
        for i in range(len(nums)):
            # avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # two pointers to look for triplet
            l = i + 1
            r = len(nums)-1
            while(l < r):
                acc = nums[i] + nums[l] + nums[r]
                # check the case
                if acc < 0:
                    l += 1
                elif acc > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while r > 0 and nums[r] == nums[r+1]:
                        r -= 1


        return output
                

                    
