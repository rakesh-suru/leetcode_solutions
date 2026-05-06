class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        rev_graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for u in range(n):
            for v in graph[u]:
                rev_graph[v].append(u)
                indegree[u] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        safe = []
        
        while queue:
            node = queue.popleft()
            safe.append(node)
            
            for nei in rev_graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return sorted(safe)