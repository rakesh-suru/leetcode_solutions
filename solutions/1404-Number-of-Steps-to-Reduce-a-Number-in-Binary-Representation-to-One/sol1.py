class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        while int(s, 2) != 1:
            if s[-1] == '1':
                s = bin(int(s, 2) + 1)
            else:
                s = bin(int(s,2)//2)
            ans += 1
        return ans