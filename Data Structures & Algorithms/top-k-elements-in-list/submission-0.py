class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solucion buckets
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        bucket = [[] for _ in range(len(nums)+1)]

        for key in freq.keys():
            bucket[freq[key]].append(key)

        solution = []

        for i in range(len(nums),-1,-1):
            for element in bucket[i]:
                solution.append(element)
                k -= 1
                if k <= 0:
                    return solution

        return solution

        
        