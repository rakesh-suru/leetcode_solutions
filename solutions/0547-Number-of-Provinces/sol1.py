class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(node):
            visited.add(node)
            
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        ans = 0
        
        for i in range(len(isConnected)):
            if i not in visited:
                ans += 1
                dfs(i)
                
        return ans