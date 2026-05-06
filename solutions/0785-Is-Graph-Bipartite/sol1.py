class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        
        for start in range(n):
            if colors[start] != -1:
                continue
            
            queue = deque([start])
            colors[start] = 0
            
            while queue:
                curr = queue.popleft()
                
                for neighbor in graph[curr]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[curr]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[curr]:
                        return False
        
        return True