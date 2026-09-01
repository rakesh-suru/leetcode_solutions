from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)
        subsets = []

        for mask in range(1, 1 << n):
            cur_lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    cur_lcm = cur_lcm // gcd(cur_lcm, coins[i]) * coins[i]

            subsets.append((cur_lcm, bits))

        def count(x):
            ans = 0

            for lcm_value, bits in subsets:

                if lcm_value > x:
                    continue

                if bits % 2:
                    ans += x // lcm_value
                else:
                    ans -= x // lcm_value

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