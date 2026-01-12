class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            a2 = a * a
            for b in range(1, n + 1):
                s = a2 + b * b
                c = isqrt(s)
                if c * c == s and c <= n:
                    ans += 1
        return ans