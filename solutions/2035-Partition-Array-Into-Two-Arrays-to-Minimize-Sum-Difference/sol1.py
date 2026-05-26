class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")

        def solve(idx, nums1, nums2):
            nonlocal ans
            if idx == n:
                if len(nums1) == len(nums2):
                    ans = min(ans, abs(sum(nums1) - sum(nums2)))
                
                return
            
            temp = nums1
            temp.append(nums[idx])
            solve(idx + 1, temp, nums2)
            nums1 = temp
            nums1.pop()

            temp = nums2
            temp.append(nums[idx])
            solve(idx + 1, nums1, temp)
            nums2 = temp
            nums2.pop()
        
        solve(0, [], [])
        return ans