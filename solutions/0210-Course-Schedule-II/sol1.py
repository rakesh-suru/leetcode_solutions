class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        stack = []

        while queue:
            node = queue.popleft()
            stack.append(node)
            count += 1
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return stack if count == numCourses else []