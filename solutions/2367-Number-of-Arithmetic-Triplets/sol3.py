class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        num_set = set(nums)
        for nums in nums:
            if nums + diff in num_set and nums + 2 * diff in num_set:
                ans += 1
        return ans