class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count(goal):
            if goal < 0:
                return 0

            l = 0
            r = 0
            sum = 0
            cnt = 0

            while r < len(nums):
                sum += nums[r]

                while sum > goal:
                    sum -= nums[l]
                    l += 1

                cnt += (r - l + 1)
                r += 1
            
            return cnt
        
        return count(goal) - count(goal - 1)