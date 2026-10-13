class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = sorted((abs(x) for x in nums), reverse=True)
        left, right = 0, len(arr) - 1
        ans = 0

        while left < right:
            ans += arr[left] ** 2 - arr[right] ** 2
            left += 1
            right -= 1

        if left == right:
            ans += arr[left] ** 2

        return ans
