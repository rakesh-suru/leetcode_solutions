class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans = sorted(s, reverse = True)
        return "".join(ans[1:]) + "1"
