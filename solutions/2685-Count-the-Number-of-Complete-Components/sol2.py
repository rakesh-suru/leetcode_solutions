class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]):

        graph = defaultdict(list)
        edgeSet = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            edgeSet.add((u, v))
            edgeSet.add((v, u))

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

            complete = True

            for i in range(len(comp)):
                for j in range(i + 1, len(comp)):
                    if (comp[i], comp[j]) not in edgeSet:
                        complete = False
                        break
                if not complete:
                    break

            if complete:
                ans += 1

        return ans