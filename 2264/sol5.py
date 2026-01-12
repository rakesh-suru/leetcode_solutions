class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for d in range(9, -1, -1):
            if str(d)*3 in num:
                return str(d)*3
        return ""
