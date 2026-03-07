class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 0
        while i < len(s) and s[i] != '0':
            i += 1
        
        while i < len(s) and s[i] == '0':
            i += 1
        
        return i == len(s)