class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        visited = [False] * n
        pathVisited = [False] * n
        safe = [False] * n
        
        def dfs(node):
            visited[node] = True
            pathVisited[node] = True
            
            for nei in graph[node]:
                if not visited[nei]:
                    if dfs(nei):
                        return True
                elif pathVisited[nei]:
                    return True
            
            pathVisited[node] = False
            safe[node] = True
            return False
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        result = []
        for i in range(n):
            if safe[i]:
                result.append(i)
        
        return result