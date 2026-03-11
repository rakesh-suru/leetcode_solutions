class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ (2 ** (len(bin(n)[2:])) - 1)