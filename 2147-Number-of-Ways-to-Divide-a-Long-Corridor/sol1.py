class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        n = len(corridor)

        def dfs(i, seats):
            if i == n:
                return 1 if seats == 2 else 0

            res = 0

            if corridor[i] == 'S':
                if seats == 2:
                    res = dfs(i + 1, 1)
                else:
                    res = dfs(i + 1, seats + 1)

            else:
                if seats == 2:
                    res = (dfs(i + 1, 0) + dfs(i + 1, 2)) % MOD
                else:
                    res = dfs(i + 1, seats)

            return res % MOD

        return dfs(0, 0)
