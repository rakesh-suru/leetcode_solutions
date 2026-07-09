class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        graph = [[] for _ in range(n)]

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                graph[i].append(i - 1)
                graph[i - 1].append(i)

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