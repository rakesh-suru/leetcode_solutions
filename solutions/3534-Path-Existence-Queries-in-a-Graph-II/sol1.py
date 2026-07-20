class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= maxDiff:
                    graph[i].append(j)
                    graph[j].append(i)

        ans = []

        for src, dest in queries:

            dist = [-1] * n
            dist[src] = 0

            q = deque([src])

            while q:

                node = q.popleft()

                if node == dest:
                    break

                for nei in graph[node]:
                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        q.append(nei)

            ans.append(dist[dest])

        return ans