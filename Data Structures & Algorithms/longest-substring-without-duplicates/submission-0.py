class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        options = {}
        left = 0
        output = 0
        char_n = 0
        for right in range(len(s)):
            if s[right] in options and options[s[right]] >= left:
                left = options[s[right]] + 1
                options[s[right]] = right
                char_n = right-left+1
            else:
                options[s[right]] = right
                char_n += 1
                output = max(output,char_n)

        return output
            

        