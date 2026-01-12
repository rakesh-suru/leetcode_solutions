class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        limit = n * n
        for a in range(1, n + 1):
            a2 = a * a
            for b in range(1, n + 1):
                s = a2 + b * b
                if s > limit:
                    continue
                c = isqrt(s)
                if c * c == s:
                    ans += 1
        return ans