class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        pq = []
        distance = [float("inf")] * n
        ways = [0] * n
        graph = defaultdict(list)

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        
        distance[0] = 0
        ways[0] = 1
        heapq.heappush(pq, (0, 0))

        while pq:
            dis, node = heapq.heappop(pq)

            for nei, d in graph[node]:

                if dis > distance[node]:
                    continue

                elif dis + d < distance[nei]:
                    distance[nei] = dis + d
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (dis + d, nei))
                
                elif dis + d == distance[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[n - 1] % MOD
