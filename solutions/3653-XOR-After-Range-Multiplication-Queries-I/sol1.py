class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        for l, r, k, v in queries:
            idx = l

            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        
        return ans
