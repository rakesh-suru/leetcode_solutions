class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        freq = Counter(nums)
        count = 0
        for num in nums:
            if freq[num + diff] > 0 and freq[num + 2 * diff] > 0:
                count += 1
        return count
