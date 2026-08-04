class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            best = -float("inf")
            curr = 0

            for j in range(i, min(i + 3, n)):
                curr += stoneValue[j]
                best = max(best, curr - dp[(j + 1) % 4])

            dp[i % 4] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"