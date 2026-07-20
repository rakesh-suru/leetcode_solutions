class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n // 2):
            c = min(s[i], s[n - i - 1])
            s[i] = s[n - i - 1] = c

        return "".join(s)
                