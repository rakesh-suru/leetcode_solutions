class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_cnt = cnt.most_common(1)[0][1]
        return sum(v for v in cnt.values() if v == max_cnt)
