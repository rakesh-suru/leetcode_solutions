class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - i - 1]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            diff[2] += 2

            diff[low] -= 1

            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

            diff[high + 1] += 1

        ans = float('inf')

        curr = 0

        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            ans = min(ans, curr)

        return ans