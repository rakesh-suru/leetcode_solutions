class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hasIncoming = set()

        for u, v in edges:
            hasIncoming.add(v)

        ans = []

        for i in range(n):
            if i not in hasIncoming:
                ans.append(i)

        return ans