class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            cnt = defaultdict(int)

            for j in range(i, n):
                cnt[nums[j]] += 1

                if cnt[nums[j]] > k:
                    break

                ans = max(ans, j - i + 1)

        return ans