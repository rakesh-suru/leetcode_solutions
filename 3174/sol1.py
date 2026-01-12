class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)