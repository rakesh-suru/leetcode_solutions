class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        l, r, maxf = 0, 0, 0
        temphash = {}
        
        while r < len(s):
            temphash[s[r]] = temphash.get(s[r], 0) + 1
            maxf = max(maxf, temphash[s[r]])

            while ((r-l+1) - maxf) > k:
                temphash[s[l]] -= 1
                maxf = 0

                for i in temphash:
                    maxf = max(maxf, temphash[i])
                
                l += 1
            
            if ((r-l+1) - maxf) <= k:
                maxlen = max(maxlen, r - l + 1)

            r += 1
        return maxlen