class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        prefix = 0
        longest = -1
        seen = {0: -1}

        for i in range(n):
            prefix += nums[i]

            if prefix - target in seen:
                length = i - seen[prefix - target]
                longest = max(longest, length)

            if prefix not in seen:
                seen[prefix] = i

        return -1 if longest == -1 else n - longest