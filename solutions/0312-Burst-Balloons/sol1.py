class Solution:
    def maxCoins(self, nums: List[int]):

        def solve(temp):
            if not temp:
                return 0

            m = len(temp)
            maxi = 0

            for i in range(m):

                left = temp[i - 1] if i > 0 else 1
                right = temp[i + 1] if i < m - 1 else 1

                coins = left * temp[i] * right

                val = coins + solve(temp[:i] + temp[i + 1:])

                maxi = max(maxi, val)

            return maxi

        return solve(nums)