class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if stack and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)
            if not stack:
                count += 1
        return count
