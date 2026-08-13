class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)
        
        visited = [False] * n

        def dfs(node):
           
            for adj in graph[node]:
                if not visited[adj]:
                    visited[adj] = True
                    dfs(adj)
        
        visited[k] = True
        dfs(k)
        ans = []

        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))

        ans = []
        for i in range(n):
            if not visited[i]:
                ans.append(i)

        return ans