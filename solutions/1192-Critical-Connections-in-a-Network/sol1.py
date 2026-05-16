class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        low = [-1] * n
        tin = [-1] * n

        timer = 1
        ans = []

        def dfs(node, parent):
            nonlocal timer

            visited[node] = True

            tin[node] = low[node] = timer
            timer += 1

            for nei in graph[node]:

                if nei == parent:
                    continue

                if not visited[nei]:

                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])

                    if low[nei] > tin[node]:
                        ans.append([node, nei])

                else:
                    low[node] = min(low[node], tin[nei])

        dfs(0, -1)

        return ans