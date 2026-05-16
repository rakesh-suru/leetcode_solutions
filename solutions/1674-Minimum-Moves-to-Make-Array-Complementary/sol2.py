class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        n = len(nums)

        ans = float('inf')

        for target in range(2, 2 * limit + 1):

            moves = 0

            for i in range(n // 2):

                left = nums[i]
                right = nums[n - i - 1]

                curr = left + right

                if curr == target:
                    continue

                elif 1 <= target - left <= limit:
                    moves += 1

                elif 1 <= target - right <= limit:
                    moves += 1

                else:
                    moves += 2

            ans = min(ans, moves)

        return ans