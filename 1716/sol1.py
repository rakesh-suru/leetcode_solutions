class Solution:
    def totalMoney(self, n: int) -> int:
        base = 0
        ans = 0
        for i in range(1, n+1):
            if i % 7 == 0:
                temp = i % 7 + base + 7
                ans += temp
                base += 1
                continue
            temp = i % 7 + base
            ans += temp
        return ans