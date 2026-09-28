class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = []

        for char in s:

            if char != ")":
                stack.append(char)

            else:
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()

                for char in temp:
                    stack.append(char)
                temp = []
        
        return "".join(stack)