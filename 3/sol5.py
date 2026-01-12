class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = maxlen = 0
        
        for r, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1
            maxlen = max(maxlen, r - l + 1)
            last_seen[ch] = r
            
        return maxlen
