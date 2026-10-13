class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""

        for char in s:
            if char == "*":
                ans = ans[:-1]
            else:
                ans += char

        return ans