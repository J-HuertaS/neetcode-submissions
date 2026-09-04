class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid

            # parte izquierda ordenada
            if nums[l] <= nums[mid]: 
                # target dentro de ese rango
                if nums[l] <= target < nums[mid]: 
                    r = mid - 1
                    continue
            else: # parte izquierda desordenada
                # target dentro del rango de alguna forma
                if target >= nums[l] or target < nums[mid]:
                    r = mid - 1
                    continue

            # si no, se toma el otro lado
            l = mid + 1

        return -1
            
        

            

        