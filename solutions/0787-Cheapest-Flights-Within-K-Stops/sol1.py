class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        dist = [float("inf")] * n
        dist[src] = 0
        
        queue = deque()
        queue.append((src, 0, 0))
        
        while queue:
            node, cost, stops = queue.popleft()
            
            if stops > k:
                continue
            
            for nei, price in graph[node]:
                new_cost = cost + price
                
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    queue.append((nei, new_cost, stops + 1))
        
        return -1 if dist[dst] == float("inf") else dist[dst]