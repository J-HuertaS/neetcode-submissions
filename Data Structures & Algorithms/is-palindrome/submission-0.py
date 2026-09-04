class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = ''.join(char for char in s if char.isalnum()).lower()
        return cleanString == cleanString[::-1]

        