class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def solve(k):
            l = 0
            ans = 0
            mapper = {}

            for r in range(len(nums)):
                mapper[nums[r]] = mapper.get(nums[r], 0) + 1

                while len(mapper) > k:
                    mapper[nums[l]] -= 1
                    if mapper[nums[l]] == 0:
                        del mapper[nums[l]]
                    l += 1
                ans += (r - l + 1)
            return ans
        return solve(k) - solve(k - 1)