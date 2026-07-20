class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        arr = sorted((nums[i], i) for i in range(n))

        values = [x for x, _ in arr]

        graph = [[] for _ in range(n)]

        for pos, (val, idx) in enumerate(arr):

            L = bisect_left(values, val - maxDiff)
            R = bisect_right(values, val + maxDiff)

            for k in range(L, R):
                if k == pos:
                    continue
                graph[idx].append(arr[k][1])

        def bfs(src, dest):

            if src == dest:
                return 0

            vis = [False] * n
            vis[src] = True

            q = deque([(src, 0)])

            while q:
                node, dist = q.popleft()

                for nei in graph[node]:

                    if not vis[nei]:

                        if nei == dest:
                            return dist + 1

                        vis[nei] = True
                        q.append((nei, dist + 1))

            return -1

        return [bfs(u, v) for u, v in queries]