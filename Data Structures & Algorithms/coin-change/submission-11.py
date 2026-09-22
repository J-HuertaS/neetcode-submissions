class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):

            if amount == 0:
                return 0

            if amount <= 0:
                return -1

            output = float('inf')

            if amount in memo:
                return memo[amount]

            for i in coins:
                temp = dfs(amount-i)     
                if temp == -1:
                    continue   
                output = min(output,temp)

            output = -1 if output == float('inf') else output + 1

            memo[amount] = output

            return output
            
            
        return dfs(amount)