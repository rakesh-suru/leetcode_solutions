class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        cnt = Counter(nums)
        for num in cnt:
            if cnt[num] == n:
                return num