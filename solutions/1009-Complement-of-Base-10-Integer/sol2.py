class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = (1 << len(bin(n)[2:])) - 1
        return n ^ mask