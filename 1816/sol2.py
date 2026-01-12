class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = ""
        for i in s:
            if i == " ":
                k -= 1
            if k == 0:
                break
            ans += i
        return ans