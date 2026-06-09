class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i < 0:
                return j + 1
            
            if j < 0:
                return i + 1
            
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = solve(i - 1, j - 1)
                return dp[i][j]

            insert = 1 + solve(i, j - 1)
            delete = 1 + solve(i - 1, j)
            replace = 1 + solve(i - 1, j - 1)

            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
        
        return solve(m - 1, n - 1)