class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] != check[char]:
                    return False
                stack.pop()
        
        if len(stack) == 0:
            return True
        return False