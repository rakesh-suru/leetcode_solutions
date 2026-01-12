class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l, r = 0, len(nums) - 1
        found = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                found = mid
                break

        if found == -1:
            return []

        first = found
        while first > 0 and nums[first - 1] == target:
            first -= 1

        ans = []
        i = first
        while i < len(nums) and nums[i] == target:
            ans.append(i)
            i += 1

        return ans
