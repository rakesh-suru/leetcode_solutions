class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        return sum(v for k,v in cnt.items() if v == max_cnt)
