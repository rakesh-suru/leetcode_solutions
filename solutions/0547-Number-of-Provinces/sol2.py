class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        for i in range(n):
            if i not in visited:
                provinces += 1
                
                queue = deque([i])
                visited.add(i)
                
                while queue:
                    node = queue.popleft()
                    
                    for neighbor in range(n):
                        if isConnected[node][neighbor] == 1 and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return provinces