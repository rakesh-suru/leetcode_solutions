class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_dig(num):
            ans = 0
            while num:
                rem = num % 10
                ans += rem
                num = num // 10
            return ans
        
        for i, num in enumerate(nums):
            if i == sum_dig(num):
                return i
        return -1