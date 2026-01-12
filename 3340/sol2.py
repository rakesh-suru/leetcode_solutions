class Solution:
    def isBalanced(self, num: str) -> bool:
        ans = 0
        temp = 1
        for n in num:
            ans += temp * int(n)
            temp *= -1   # flip sign each time
        return ans == 0
