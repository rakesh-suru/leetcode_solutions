class Solution:
    def maxDistinct(self, s: str) -> int:
        temp = []
        for c in s:
            if c not in temp:
                temp.append(c)
        return len(temp)