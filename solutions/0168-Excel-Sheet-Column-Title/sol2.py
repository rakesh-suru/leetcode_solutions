class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        ans = 0
        pos = 0

        while n:
            if n & 1:
                if prev != -1:
                    ans = max(ans, pos - prev)
                prev = pos
            pos += 1
            n >>= 1

        return ans