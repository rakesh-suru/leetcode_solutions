class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        pairs = {}
        ans = ""

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                j = stack.pop()
                pairs[i] = j
                pairs[j] = i
        
        i = 0
        move = 1
        ans = []

        while i < len(s):
            if s[i] == "(" or s[i] == ")":
                i = pairs[i]
                move = -move
            
            else:
                ans.append(s[i])
            
            i += move
        
        return "".join(ans)