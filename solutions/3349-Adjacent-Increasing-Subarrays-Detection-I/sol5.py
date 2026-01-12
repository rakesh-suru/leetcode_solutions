class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        left = 0
    
        while left < len(nums):
            if len(nums) - left < 2 * k:
                break

            for i in range(left+1,left+k):
                if nums[i] <= nums[i-1]:
                    break
            else:
                for i in range(left+k+1, left+k+k):
                    if nums[i] <= nums[i-1]:
                        break
                else:
                    return True

            left += 1
        return False