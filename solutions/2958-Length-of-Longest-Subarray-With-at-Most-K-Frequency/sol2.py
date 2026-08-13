class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)

        for right in range(len(nums)):
            cnt[nums[right]] += 1

            while cnt[nums[right]] > k:
                cnt[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans