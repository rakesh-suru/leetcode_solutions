class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        if k >= len(num):
            return "0"

        for n in num:
            if not stack:
                stack.append(n)
            else:
                while k and stack and stack[-1] > n:
                    stack.pop()
                    k -= 1
                stack.append(n)
        
        while k:
            stack.pop()
            k -= 1
        
        res =  "".join(stack).lstrip("0")
        return res if res else "0"