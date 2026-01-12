import re

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        matches = re.findall(r'(\d)\1\1', num)
        return max((d*3 for d in matches), default="")
