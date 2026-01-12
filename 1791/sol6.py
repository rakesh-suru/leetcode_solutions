class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x=set(edges[0])
        y=set(edges[1])
        z=list(x&y)
        return z[0]