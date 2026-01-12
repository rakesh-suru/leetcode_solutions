class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            hashmap = {}
            for j in range(i, len(s)):
                if s[j] not in hashmap:
                    hashmap[s[j]] = 1
                    length = j - i + 1
                    maxlen = max(maxlen, length)
                else:
                    break
        return maxlen