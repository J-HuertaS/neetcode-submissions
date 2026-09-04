class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        options = set(nums)
        output = 0
        for element in options:
            if element-1 in options:
                continue
            acc = 1
            base = element
            while(base+1 in options):
                base += 1
                acc += 1
            
            output = max(output,acc)

        return output
        