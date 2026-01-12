class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum((1 if i % 2 == 0 else -1) * int(d) for i, d in enumerate(num)) == 0
