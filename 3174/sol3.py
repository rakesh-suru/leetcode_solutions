class Solution:
    def clearDigits(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch.isdigit():
                result = result[:-1]
            else:
                result += ch
        return result
