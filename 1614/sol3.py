class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for change in map(lambda x: 1 if x=="(" else -1 if x==")" else 0, s):
            depth += change
            max_depth = max(max_depth, depth)
        return max_depth
