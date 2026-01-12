class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            j, k = i + 1, i + 2
            while j < n and nums[j] - nums[i] < diff:
                j += 1
            if j < n and nums[j] - nums[i] == diff:
                while k < n and nums[k] - nums[j] < diff:
                    k += 1
                if k < n and nums[k] - nums[j] == diff:
                    count += 1
        return count
