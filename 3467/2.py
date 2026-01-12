class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)
        return sorted(ans)