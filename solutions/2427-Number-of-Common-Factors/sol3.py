class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        ans = 0

        for i in range(1, int(g ** 0.5) + 1):
            if g % i == 0:
                ans += 1
                if i != g // i:
                    ans += 1

        return ans