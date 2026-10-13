class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = sorted(abs(x) for x in nums)[::-1]
        n = len(arr)
        k = (n + 1) // 2

        ans = 0
        for i in range(n):
            if i < k:
                ans += arr[i] ** 2
            else:
                ans -= arr[i] ** 2

        return ans
