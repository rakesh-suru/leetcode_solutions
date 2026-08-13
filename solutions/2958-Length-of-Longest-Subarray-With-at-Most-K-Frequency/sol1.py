class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        right = 0
        n = len(nums)
        cnt = defaultdict(int)

        while left <= right < n:
            cnt[nums[right]] += 1

            while cnt[nums[right]] > k and left <= right:
                cnt[nums[left]] -= 1
                left += 1

            right += 1
            ans = max(ans, right - left)
            
        return ans