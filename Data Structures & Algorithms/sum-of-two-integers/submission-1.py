class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFF
        MAX_INT = 0x7FF

        while b != 0:
            carry = (a&b) & mask
            a = (a ^ b) & mask
            b = (carry) << 1 & mask

        return a if a <= MAX_INT else ~(a ^ mask)
        