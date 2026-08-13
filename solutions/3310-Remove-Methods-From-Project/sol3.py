class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]):

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        visited = [False] * n
        stack = [k]
        visited[k] = True

        while stack:
            node = stack.pop()

            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)

        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))

        return [i for i in range(n) if not visited[i]]