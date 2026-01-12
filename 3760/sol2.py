class Solution:
    def maxDistinct(self, s: str) -> int:
        temp = set()
        for c in s:
            temp.add(c)
        return len(temp)