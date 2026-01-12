class Solution:
    def countAsterisks(self, s: str) -> int:
        stack = []
        ans = 0
        for ch in s:
            if ch == "|":
                if stack and stack[-1] == "|":
                    stack.pop()
                else:
                    stack.append("|")
            elif ch == "*" and not stack:
                ans += 1
        return ans
