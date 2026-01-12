class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            for j in range(1, n+1):
                temp = sqrt(i*i + j*j)
                if temp == int(temp) and temp <= n:
                    ans += 1
        return ans