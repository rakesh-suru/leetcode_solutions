class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        active = 0

        flips = [0] * n

        for i in range(n):
            if i >= 3:
                active ^= flips[i - 3]

            current = nums[i] ^ active

            if current == 0:
                if i + 2 >= n:
                    return -1

                ans += 1
                active ^= 1
                flips[i] = 1

        return ans