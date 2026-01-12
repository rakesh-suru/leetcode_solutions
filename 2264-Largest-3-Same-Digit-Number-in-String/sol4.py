class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for d in map(str, range(9, -1, -1)):
            if d*3 in num:
                return d*3
        return ""
