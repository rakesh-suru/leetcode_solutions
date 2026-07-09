class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for idx in range(n - 1, -1, -1):
            length = 0
            maxi = -float("inf")
            ans = -float("inf")

            for i in range(idx, min(n, idx + k)):
                length += 1
                maxi = max(maxi, arr[i])

                total = length * maxi + dp[i + 1]
                ans = max(ans, total)

            dp[idx] = ans

        return dp[0]