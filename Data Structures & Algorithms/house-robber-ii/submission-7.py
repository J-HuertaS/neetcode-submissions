class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        segment1 = nums[1:]
        segment2 = nums[:-1]

        def robLocal(n: List[int]) -> int:

            if len(n) == 1:
                return n[0]

            output = [0 for _ in range(len(n)+1)]

            output[1] = n[0]

            for i in range(2,len(output)):
                temp = max(output[i-1],output[i-2]+n[i-1])
                output[i] = temp

            return output[len(n)]

        return max(robLocal(segment1),robLocal(segment2))

        