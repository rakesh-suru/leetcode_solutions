class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter(nums)
        max_cnt = 1
        for num in cnt:
            max_cnt = max(max_cnt, cnt[num])
        
        for num in cnt:
            if cnt[num] == max_cnt:
                ans += cnt[num]
        
        return ans