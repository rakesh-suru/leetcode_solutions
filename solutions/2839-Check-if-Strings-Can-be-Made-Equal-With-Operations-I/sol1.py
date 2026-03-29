class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        temp = s1[2] + s1[1] + s1[0] + s1[3]
        if temp == s2:
            return True
        
        temp = s1[0] + s1[3] + s1[2] + s1[1]
        if temp == s2:
            return True
        
        temp = s1[2] + s1[3] + s1[0] + s1[1]
        return temp == s2