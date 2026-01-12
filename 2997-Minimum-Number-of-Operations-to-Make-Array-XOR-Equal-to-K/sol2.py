class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = k
        for num in nums:
            ans ^= num
        return bin(ans).count("1")