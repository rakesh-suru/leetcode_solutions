class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        a = 0
        b = a + k

        while a + 2 * k <= len(nums):
            if (nums[a:a+k] == sorted(nums[a:a+k]) and len(set(nums[a:a+k])) == k and
                nums[b:b+k] == sorted(nums[b:b+k]) and len(set(nums[b:b+k])) == k):
                return True
            a += 1
            b = a + k
        return False
