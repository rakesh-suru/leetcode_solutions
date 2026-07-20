class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node, component):
            visited[node] = True
            component.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, component)

        ans = 0

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)

                nodes = len(component)

                edge_count = 0
                for node in component:
                    edge_count += len(graph[node])

                edge_count //= 2

                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans