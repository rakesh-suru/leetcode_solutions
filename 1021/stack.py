class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        stack = []
        for i in s:
            if len(stack) == 0 and i == "(":
                stack.append(i)
            elif len(stack) == 1 and i == ")":
                stack.pop()
            else:
                if i == "(":
                    stack.append(i)
                else:
                    stack.pop()
                ans.append(i)
        return "".join(ans)