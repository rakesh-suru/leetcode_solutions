class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        l = len(cuts)
        cuts.sort()
        cuts = [0] + cuts + [n]

        dp = [[-1] * (l + 2) for _ in range(l + 2)]

        def solve(i ,j):
            if i > j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            mini = float("inf")
            for k in range(i, j + 1):
                cost = cuts[j + 1] - cuts[i - 1] + solve(i, k - 1) + solve(k + 1, j)
                mini = min(cost, mini)
            
            dp[i][j] = mini
            return dp[i][j]
        

        return solve(1, l)