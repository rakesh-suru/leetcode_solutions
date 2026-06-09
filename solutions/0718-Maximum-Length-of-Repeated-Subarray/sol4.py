class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[-1] * n for _ in range(m)]
        ans = 0

        def solve(i, j):
            nonlocal ans

            if i == m or j == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + solve(i + 1, j + 1)
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0

            solve(i + 1, j)
            solve(i, j + 1)

            return dp[i][j]

        solve(0, 0)
        return ans