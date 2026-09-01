class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarrays = []
        left = 0
        right = k
        n = len(nums)

        while right <= n:
            subarrays.append(nums[left:right])
            left += 1
            right += 1
        
        ans = -1
        for num in nums:
            cnt = 0
            for sub in subarrays:
                if num in sub:
                    cnt += 1
            if cnt == 1:
                ans = max(ans, num)
        return ans