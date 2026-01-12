class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()

                if i == ")" and ch != "(":
                    return False
                if i == "}" and ch != "{":
                    return False
                if i == "]" and ch != "[":
                    return False

        return len(stack) == 0
