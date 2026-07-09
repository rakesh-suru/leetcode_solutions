class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def solve(idx):
            if idx == n:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            length = 0
            maxi = -float("inf")
            ans = -float("inf")

            for i in range(idx, min(n, idx + k)):
                length += 1
                maxi = max(maxi, arr[i])

                total = length * maxi + solve(i + 1)
                ans = max(ans, total)

            dp[idx] = ans
            return ans

        return solve(0)