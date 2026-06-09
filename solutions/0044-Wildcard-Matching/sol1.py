class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        def solve(i, j):
            if i < 0 and j < 0:
                return True

            if j < 0:
                return False

            if i < 0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True

            if s[i] == p[j] or p[j] == '?':
                return solve(i - 1, j - 1)

            if p[j] == '*':
                return solve(i - 1, j) or solve(i, j - 1)

            return False

        return solve(n - 1, m - 1)