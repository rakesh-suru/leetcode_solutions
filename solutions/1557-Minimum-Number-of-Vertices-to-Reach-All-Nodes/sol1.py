class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0] * n
        for u, v in edges:
            incoming[v] += 1
        
        ans = []
        for i, count in enumerate(incoming):
            if count == 0:
                ans.append(i)
        return ans