class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        def solve(left, right, p1, p2, chance):
            if left > right:
                return p1 >= p2

            if chance:
                return (
                    solve(left + 1, right, p1 + nums[left], p2, False)
                    or
                    solve(left, right - 1, p1 + nums[right], p2, False)
                )
            else:
                return (
                    solve(left + 1, right, p1, p2 + nums[left], True)
                    and
                    solve(left, right - 1, p1, p2 + nums[right], True)
                )

        return solve(0, n - 1, 0, 0, True)