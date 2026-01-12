class Solution:
    def isBalanced(self, num: str) -> bool:
        even = sum(int(a) for a in num[::2])
        odd  = sum(int(b) for b in num[1::2])
        return even == odd
