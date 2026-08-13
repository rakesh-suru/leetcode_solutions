class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]):

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        visited = [False] * n
        q = deque([k])
        visited[k] = True

        while q:
            node = q.popleft()

            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))

        return [i for i in range(n) if not visited[i]]