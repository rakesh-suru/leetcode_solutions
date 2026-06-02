class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans = 0

        for num in nums:
            ans += str(num).count(str(digit))
        
        return ans