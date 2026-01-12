class Solution:
    def reverseDegree(self, s: str) -> int:
        val = ord('z') + 1
        return sum((i + 1) * (val - ord(c)) for i, c in enumerate(s))
