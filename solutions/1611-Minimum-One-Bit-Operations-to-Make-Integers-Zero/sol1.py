class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        num = bin(n)[2:]

        def rightmost(s: str) -> str:
            if not s:
                return s
            arr = list(s)
            arr[-1] = '0' if arr[-1] == '1' else '1'
            return ''.join(arr)

        def change(s: str, i: int) -> str:
            if not (0 <= i < len(s)):
                return s
            arr = list(s)
            arr[i] = '0' if arr[i] == '1' else '1'
            return ''.join(arr)

        def min_ops_from_bits(bits: str) -> int:
            x = int(bits, 2)
            ans = 0
            while x:
                ans ^= x
                x >>= 1
            return ans

        return min_ops_from_bits(num)
