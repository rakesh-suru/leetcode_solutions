class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        vis = [False] * (n + 1)

        def dfs(node):
            vis[node] = True
            res = float("inf")

            for nei, wt in adj[node]:
                res = min(res, wt)

                if not vis[nei]:
                    res = min(res, dfs(nei))

            return res

        return dfs(1)