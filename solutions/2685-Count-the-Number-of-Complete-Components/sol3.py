class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node, comp):
            visited[node] = True
            comp.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, comp)

        ans = 0

        for i in range(n):

            if visited[i]:
                continue

            comp = []
            dfs(i, comp)

            size = len(comp)

            good = True

            for node in comp:
                if len(graph[node]) != size - 1:
                    good = False
                    break

            if good:
                ans += 1

        return ans