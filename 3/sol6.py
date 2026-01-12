class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        l = maxlen = 0
        
        for r, ch in enumerate(s):
            idx = ord(ch)
            if last_seen[idx] >= l:
                l = last_seen[idx] + 1
            maxlen = max(maxlen, r - l + 1)
            last_seen[idx] = r
            
        return maxlen
