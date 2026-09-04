class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += str(len(i))
            output += "$"
            output += i
        
        print(output)

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        l = 0
        while l < len(s):
            length = ""
            while l < len(s) and s[l] != "$":
                length += s[l]
                l += 1
            jump = int(length)
            output.append(s[l+1:l+jump+1])
            l += jump + 1

        return output

