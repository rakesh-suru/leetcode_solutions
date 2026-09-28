class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        def solve(idx):
            if idx == n:
                return 1

            seen = set()
            count = 1

            for i in range(idx, n):
                if s[i] not in seen:
                    seen.add(s[i])
                    count += solve(i + 1)

            return count

        return (solve(0) - 1) % MOD