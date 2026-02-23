class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        curr = 0
        ans = 0

        for num in nums:
            curr += num
            rem = curr - k
            ans += prefix.get(rem, 0)
            prefix[curr] = prefix.get(curr, 0) + 1
        
        return ans