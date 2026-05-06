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
        
        safe = [False] * n
        
        while queue:
            node = queue.popleft()
            safe[node] = True
            
            for nei in rev_graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        result = []
        for i in range(n):
            if safe[i]:
                result.append(i)
        
        return sorted(result)