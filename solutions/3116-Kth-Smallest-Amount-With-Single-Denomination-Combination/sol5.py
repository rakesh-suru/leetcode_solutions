from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            for mask in range(1, 1 << n):

                cur_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        cur_lcm = lcm(cur_lcm, coins[i])
                        bits += 1

                        if cur_lcm > x:
                            break

                else:
                    if bits % 2 == 1:
                        ans += x // cur_lcm
                    else:
                        ans -= x // cur_lcm

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left