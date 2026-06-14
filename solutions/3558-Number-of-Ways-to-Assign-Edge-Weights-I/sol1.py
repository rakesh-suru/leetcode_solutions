class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        tree = defaultdict(list)
        MOD = 10 ** 9 + 7

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        max_depth = 0
        visited = set()

        def dfs(node, depth):
            nonlocal max_depth

            visited.add(node)

            leaf = True

            for adj in tree[node]:
                if adj not in visited:
                    leaf = False
                    dfs(adj, depth + 1)

            if leaf:
                max_depth = max(max_depth, depth)

        dfs(1, 0)

        return (2 ** (max_depth - 1)) % MOD