class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        counter = [0]
        
        def dfs(s,idx):
            if len(s) - idx <= 0:
                return 1

            if s[idx] == "0":
                return 0

            if len(s) - idx == 1:
                return 1

            if s[idx] not in {"1","2"} or (s[idx] == "2" and s[idx+1] in {"7","8","9"}):
                if s[idx:] in memo:
                    return memo[s[idx:]]

                temp = dfs(s,idx+1)

                memo[s[idx:]] = temp

                return temp

            if s[idx+1:] in memo:
                first = memo[s[idx+1:]]
            else: 
                first = dfs(s,idx+1)
                memo[s[idx+1:]] = first

            if s[idx+2:] in memo:
                second = memo[s[idx+2:]]
            else: 
                second = dfs(s,idx+2)
                memo[s[idx+2:]] = second

            return first + second

        return dfs(s,0)


            
          