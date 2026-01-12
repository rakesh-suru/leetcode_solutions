class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        n = len(s)
        l , r, maxlen = 0, 0, 0
        while(r < n):
            if s[r] in hashmap:
                if hashmap[s[r]] >= l:
                    l = hashmap[s[r]] + 1
            length = r - l + 1
            maxlen = max(length, maxlen)
            hashmap[s[r]] = r
            r += 1
        return maxlen
