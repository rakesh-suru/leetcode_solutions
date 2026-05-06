
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = [False] * numCourses
        pathVisited = [False] * numCourses
        
        def dfs(node):
            visited[node] = True
            pathVisited[node] = True
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif pathVisited[neighbor]:
                    return True

            pathVisited[node] = False
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        
        return True