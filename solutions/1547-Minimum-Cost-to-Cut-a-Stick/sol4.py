class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        m = len(cuts)

        cuts = [0] + cuts + [n]

        dp = [[0] * (m + 2) for _ in range(m + 2)]

        for i in range(m, 0, -1):
            for j in range(i, m + 1):
                mini = float("inf")

                for k in range(i, j + 1):
                    cost = (
                        cuts[j + 1] - cuts[i - 1]
                        + dp[i][k - 1]
                        + dp[k + 1][j]
                    )

                    mini = min(mini, cost)

                dp[i][j] = mini

        return dp[1][m]