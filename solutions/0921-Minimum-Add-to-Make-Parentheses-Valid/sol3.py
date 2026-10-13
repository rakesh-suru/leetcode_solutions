class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        ans = 0

        for char in s:
            if char == "(":
                opened += 1
            else:
                if opened > 0:
                    opened -= 1
                else:
                    ans += 1

        return ans + opened