class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l , r, maxlen = 0, 0, 0
        while(r < len(s)):
            if s[r] in hashmap:
                if hashmap[s[r]] >= l:
                    l = hashmap[s[r]] + 1
            length = r - l + 1
            maxlen = max(length, maxlen)
            hashmap[s[r]] = r
            r += 1
        return maxlen
