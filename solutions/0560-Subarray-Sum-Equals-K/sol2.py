class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        curr = 0
        ans = 0
        
        for i in range(len(nums)):
            curr += nums[i]
            
            if curr == k:
                ans += 1
            
            rem = curr - k
            if rem in prefix:
                ans += prefix[rem]
            
            prefix[curr] = prefix.get(curr, 0) + 1
                
        return ans
