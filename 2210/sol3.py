class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        indices = [0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                indices.append(i)

        ans = 0
        for i in range(1, len(indices) - 1):
            prev, curr, nxt = indices[i - 1], indices[i], indices[i + 1]
            if nums[prev] < nums[curr] > nums[nxt]:
                ans += 1
            elif nums[prev] > nums[curr] < nums[nxt]:
                ans += 1
        return ans
