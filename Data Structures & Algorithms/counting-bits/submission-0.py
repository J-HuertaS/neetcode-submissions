class Solution:
    def countBits(self, n: int) -> List[int]:
        def aux(idx):
            res = 0
            while idx:
                idx = idx & (idx-1)
                res += 1
            return res

        output = [0 for i in range(n+1)]

        for i in range(n+1):
            output[i] = aux(i)

        return output
        