class Solution:
    def reverse(self, n: int) -> int:
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return rev

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = float("inf")
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                ans = min(ans, i - seen[n])
            seen[self.reverse(n)] = i

        return -1 if ans == float("inf") else ans