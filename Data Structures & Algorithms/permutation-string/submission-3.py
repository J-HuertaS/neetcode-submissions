from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)

        left, right = 0, 0

        while right < len(s2):
            c[s2[right]] -= 1
            if left < right - len(s1) + 1:
                c[s2[left]] += 1
                left += 1
            if all( v == 0 for v in c.values()):
                return True
            right += 1

        return False
        