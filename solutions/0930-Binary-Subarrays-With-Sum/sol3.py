class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count(goal):
            if goal < 0:
                return 0

            l = 0
            r = 0
            curr = 0
            cnt = 0

            while r < len(nums):
                curr += nums[r]

                while curr > goal:
                    curr -= nums[l]
                    l += 1

                cnt += (r - l + 1)
                r += 1
            
            return cnt
        
        return count(goal) - count(goal - 1)