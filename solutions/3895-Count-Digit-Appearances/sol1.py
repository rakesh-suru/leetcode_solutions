class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans = 0

        for num in nums:
            temp = num
            while temp > 0:
                if temp % 10 == digit:
                    ans += 1
                temp //= 10
        
        return ans