class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            freq = defaultdict(int)
            distinct = 0

            for j in range(i, n):
                if freq[nums[j]] == 0:
                    distinct += 1
                freq[nums[j]] += 1
                ans += distinct * distinct

        return ans