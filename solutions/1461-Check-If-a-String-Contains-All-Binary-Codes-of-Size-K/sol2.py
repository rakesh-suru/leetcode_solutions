class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        l = 0
        r = k

        while r <= len(s):
            codes.add(s[l : r])
            r += 1
            l += 1
        
        if len(codes) == 2 ** k:
            return True
        return False