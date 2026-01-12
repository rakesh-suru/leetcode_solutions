class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            if "A" <= c <= "Z":
                ans += chr(ord(c) | 32)
            else:
                ans += c
        return ans
