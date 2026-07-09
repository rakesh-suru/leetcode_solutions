class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] <= maxDiff:
                    graph[i].append(j)
                    graph[j].append(i)

        ans = []

        for s, t in queries:

            vis = [False] * n
            q = deque([s])
            vis[s] = True

            while q:
                node = q.popleft()

                if node == t:
                    break

                for nei in graph[node]:
                    if not vis[nei]:
                        vis[nei] = True
                        q.append(nei)

            ans.append(vis[t])

        return ans