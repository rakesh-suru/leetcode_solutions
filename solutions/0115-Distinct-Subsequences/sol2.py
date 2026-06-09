class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        def solve(i, j):
            if j == m:
                return 1

            if i == n:
                return 0

            if s[i] == t[j]:
                return solve(i + 1, j + 1) + solve(i + 1, j)

            return solve(i + 1, j)

        return solve(0, 0)