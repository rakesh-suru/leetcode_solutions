class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def solve(num):
            prev2 = 0
            prev1 = num[0]

            for i in range(1, len(num)):

                take = num[i] + prev2
                not_take = prev1

                curr = max(take, not_take)

                prev2 = prev1
                prev1 = curr

            return prev1
        
        return max(solve(nums[1:]), solve(nums[:-1]))