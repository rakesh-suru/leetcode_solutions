class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26
        total = 0

        for ch in s:
            idx = ord(ch) - ord('a')

            new_count = total + 1

            total = (total - dp[idx] + new_count) % MOD

            dp[idx] = new_count

        return total