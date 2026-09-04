class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        lowest = float('inf')
        for i in prices:
            if i < lowest:
                lowest = i
            else:
                profit = i - lowest
                output = max(output,profit)

        return output