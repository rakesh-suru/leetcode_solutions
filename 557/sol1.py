class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        ans = ""
        for word in temp:
            ans += word[::-1]
            ans += " "
        return ans[:-1]