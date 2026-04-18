class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = float("inf")
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                ans = min(ans, i - seen[n])
            seen[int(str(n)[::-1])] = i

        return -1 if ans == float("inf") else ans
