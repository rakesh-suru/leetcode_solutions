class Solution:
    def stringHash(self, s: str, k: int) -> str:
        mapping = {chr(ord('a') + i): i for i in range(26)}
        res = []
        for i in range(0, len(s), k):
            total = sum(mapping[c] for c in s[i:i+k])
            res.append(chr(ord('a') + (total % 26)))
        return ''.join(res)