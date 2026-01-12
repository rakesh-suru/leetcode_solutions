class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        left_sum = nums[0]
        right_sum = sum(nums) - nums[0]

        for i in range(1,len(nums)):
            temp = left_sum - right_sum
            if temp % 2 == 0:
                ans += 1
            left_sum += nums[i]
            right_sum -= nums[i]
            
        return ans