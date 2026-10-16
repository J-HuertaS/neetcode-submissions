from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cont = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+len(s1)]) == cont:
                return True

        return False
        