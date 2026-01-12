class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n-2):
            for j in range(i + 1, n - 1):
                low, high = j + 1, n - 1

                while low <= high:
                    mid = (low + high) // 2
                    if nums[i] + nums[j] > nums[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                
                ans += high - j
        return ans