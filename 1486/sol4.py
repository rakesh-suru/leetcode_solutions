class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xor_to(x):
            return [x, 1, x + 1, 0][x % 4]

        a = start >> 1
        xor_part = xor_to(a - 1) ^ xor_to(a + n - 1)
        return (xor_part << 1) | ((start & 1) & (n & 1))