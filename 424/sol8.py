class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        l, maxf = 0, 0
        temphash = {}
        
        for r in range(len(s)):
            temphash[s[r]] = temphash.get(s[r], 0) + 1
            maxf = max(maxf, temphash[s[r]])

            if (r - l + 1) - maxf > k:
                temphash[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen
