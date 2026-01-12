class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(0, len(s) - 1, 2):
            res.append(s[i])
            res.append(chr(ord(s[i]) + int(s[i + 1])))
        if len(s) % 2:
            res.append(s[-1])
        return "".join(res)
