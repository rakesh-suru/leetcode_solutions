class Solution:
    def stringHash(self, s: str, k: int) -> str:
        a = ord('a')
        res = []
        for i in range(0, len(s), k):
            block = s[i:i+k]
            total = sum(ord(c) - a for c in block)
            res.append(chr(a + (total % 26)))
        return ''.join(res)
