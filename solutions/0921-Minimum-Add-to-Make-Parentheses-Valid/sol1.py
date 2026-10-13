class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0

        for char in s:
            if char == ")":
                if not stack:
                    ans += 1
                else:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(char)
            else:
                stack.append(char)
        
        while stack:
            stack.pop()
            ans += 1 

        return ans