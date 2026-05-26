class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        dp = [-1] * n

        def solve(idx):

            if dp[idx] != -1:
                return dp[idx]

            ans = 1

            for j in range(idx - 1, max(-1, idx - d - 1), -1):

                if arr[j] >= arr[idx]:
                    break

                ans = max(ans, 1 + solve(j))

            for j in range(idx + 1, min(n, idx + d + 1)):

                if arr[j] >= arr[idx]:
                    break

                ans = max(ans, 1 + solve(j))

            dp[idx] = ans
            return ans

        res = 1

        for i in range(n):
            res = max(res, solve(i))

        return res