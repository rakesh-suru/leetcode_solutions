class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l, r = 0, len(nums) - 1
        first_index = -1

        # Binary search for the first occurrence of target
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                first_index = mid
                r = mid - 1  # Keep looking to the left for first occurrence

        if first_index == -1:
            return []

        # Collect all target indices starting from first_index
        ans = []
        i = first_index
        while i < len(nums) and nums[i] == target:
            ans.append(i)
            i += 1

        return ans
