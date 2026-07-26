class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        visited = [False] * n

        def dfs(node, path):
            if node == n - 1:
                ans.append(path[:])
                return

            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    path.append(nei)
                    dfs(nei, path)
                    path.pop()

            visited[node] = False

        dfs(0, [0])
        return ans