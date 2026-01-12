class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans = sum(nums)
        for num in nums:
            if num < 10:
                ans -= num
            else:
                while num > 0:
                    r = num%10
                    ans -= r
                    num = num // 10
        return ans