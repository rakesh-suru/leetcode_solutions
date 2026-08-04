class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(left, right):
            if left == right:
                return nums[left]

            leftPick = nums[left] - solve(left + 1, right)
            rightPick = nums[right] - solve(left, right - 1)

            return max(leftPick, rightPick)

        return solve(0, len(nums) - 1) >= 0