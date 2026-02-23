class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        prefix = {}
        curr = 0
        ans = 0
        
        for i in range(len(nums)):
            curr += nums[i] % 2
            
            if curr == k:
                ans += 1
            
            rem = curr - k
            if rem in prefix:
                ans += prefix[rem]
            
            prefix[curr] = prefix.get(curr, 0) + 1
                
        return ans
