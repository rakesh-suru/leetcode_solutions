class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        d = str(digit)
        return sum(str(num).count(d) for num in nums)