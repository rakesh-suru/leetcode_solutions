class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_alpha = {chr(i): 26 - (i - ord('a')) for i in range(ord('a'), ord('z') + 1)}
        return sum((i + 1) * rev_alpha[c] for i, c in enumerate(s))