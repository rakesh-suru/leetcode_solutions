class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = {v for _, v in edges}
        return [i for i in range(n) if i not in incoming]