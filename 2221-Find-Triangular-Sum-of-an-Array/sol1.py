class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            temp = []
            for i in range(n-1):
                temp.append((nums[i] + nums[i+1]) % 10)
            for i in range(len(temp)):
                nums[i] = temp[i]
            n -= 1
        return nums[0]