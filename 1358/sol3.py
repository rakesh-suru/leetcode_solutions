class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        last_seen = [-1, -1, -1]
        
        for i, ch in enumerate(s):
            last_seen[ord(ch) - ord('a')] = i
            result += min(last_seen) + 1
        
        return result
