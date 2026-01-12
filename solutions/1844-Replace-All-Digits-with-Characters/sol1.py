class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        l = len(s)
        for i in range(0, l - 1, 2):
            letter = s[i]
            digit = int(s[i + 1])
            ans += letter
            ans += chr(ord(letter) + digit)
        if l % 2 == 1:
            ans += s[-1]
        return ans
