class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        First approach
        cleanString = ''.join(char for char in s if char.isalnum()).lower()
        return cleanString == cleanString[::-1]
        '''
        cleanString = ''.join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(cleanString)-1
        while l<r:
            if cleanString[l] != cleanString[r]:
                return False
            l += 1
            r -= 1

        return True
        

        