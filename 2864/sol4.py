class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans = sorted(s, reverse = True)
        ans.remove("1")
        return "".join(ans) + "1"
