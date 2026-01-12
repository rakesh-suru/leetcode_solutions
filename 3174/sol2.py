class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for ch in s:
            ch.isdigit() and res and res.pop() or res.append(ch)
        return "".join(res)
