class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        l, r, maxf = 0, 0, 0
        temphash = [0] * 26

        while r < len(s):
            temphash[ord(s[r]) - ord("A")] += 1
            maxf = max(maxf, temphash[ord(s[r]) - ord("A")])  

            while ((r - l + 1) - maxf) > k:
                temphash[ord(s[l]) - ord("A")] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen
