class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        n = len(corridor)

        dp = [[0]*3 for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(n):
            for s in range(3):
                if dp[i][s] == 0:
                    continue

                if corridor[i] == 'S':
                    if s == 2:
                        dp[i+1][1] = (dp[i+1][1] + dp[i][s]) % MOD
                    else:
                        dp[i+1][s+1] = (dp[i+1][s+1] + dp[i][s]) % MOD
                else:
                    if s == 2:
                        dp[i+1][0] = (dp[i+1][0] + dp[i][s]) % MOD
                        dp[i+1][2] = (dp[i+1][2] + dp[i][s]) % MOD
                    else:
                        dp[i+1][s] = (dp[i+1][s] + dp[i][s]) % MOD

        return dp[n][2]
