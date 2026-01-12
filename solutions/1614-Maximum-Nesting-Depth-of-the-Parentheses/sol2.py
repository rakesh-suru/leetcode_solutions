class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for ch in s:
            if ch == "(":
                stack.append("(")
                max_depth = max(max_depth, len(stack))
            elif ch == ")":
                stack.pop()
        return max_depth
