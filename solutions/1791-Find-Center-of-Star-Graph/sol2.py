class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = {}
        for u, v in edges:
            freq[u] = freq.get(u, 0) + 1
            freq[v] = freq.get(v, 0) + 1
        for node, count in freq.items():
            if count == len(freq) - 1:
                return node
