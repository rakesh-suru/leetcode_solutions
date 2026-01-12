class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums.sort()
        max_cnt, ans, count = 1, 0, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            max_cnt = max(max_cnt, count)

        count, res = 1, 0
        for i in range(1, len(nums)+1):
            if i < len(nums) and nums[i] == nums[i-1]:
                count += 1
            else:
                if count == max_cnt:
                    res += count
                count = 1
        return res
