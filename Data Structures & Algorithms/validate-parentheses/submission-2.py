class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for i in s:
            if i not in mp:
                stack.append(i)
            else:
                if not stack or stack.pop() != mp[i]:
                    return False
        
        return not stack
