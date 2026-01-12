class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ans = []
        for i in range(k - 1, -1, -1):
            ans.append(s[i])
        return "".join(ans) + s[k:]
