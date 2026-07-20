class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= maxDiff:
                    graph[i].append(j)
                    graph[j].append(i)

        def bfs(src, dest):
            if src == dest:
                return 0

            visited = [False] * n
            visited[src] = True

            q = deque([(src, 0)])

            while q:
                node, dist = q.popleft()

                for nei in graph[node]:
                    if not visited[nei]:
                        if nei == dest:
                            return dist + 1

                        visited[nei] = True
                        q.append((nei, dist + 1))

            return -1

        return [bfs(u, v) for u, v in queries]