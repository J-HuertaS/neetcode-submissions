class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r - 1:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                    continue
            else:
                if target >= nums[l] or target < nums[mid]:
                    r = mid - 1
                    continue

            # si no, se toma el otro lado
            l = mid + 1

        if r < len(nums) and nums[r] == target:
            return r
        elif l >= 0 and l < len(nums) and nums[l] == target:
            return l
        else:
            return -1
            
        

            

        