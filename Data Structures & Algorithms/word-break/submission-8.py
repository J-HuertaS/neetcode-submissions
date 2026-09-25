class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(index):
            if index >= len(s):
                return True

            if index in memo:
                return memo[index]

            flag = False

            for word in wordDict:
                wordLen = len(word)
                if s[index:index+wordLen] == word:
                    flag = flag or dfs(index+wordLen)

            memo[index] = flag
            

            return flag

        flag = dfs(0)
        return flag
                    