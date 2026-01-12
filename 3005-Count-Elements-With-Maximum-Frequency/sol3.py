class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        max_cnt, ans = 0, 0
        
        for num in nums:
            freq[num] += 1
            if freq[num] > max_cnt:
                max_cnt = freq[num]
                ans = freq[num]
            elif freq[num] == max_cnt:
                ans += freq[num]
        
        return ans
