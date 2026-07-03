class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        ans = []

        def solve(idx, prev, path):
            nonlocal ans

            if idx == n:
                if len(path) > len(ans):
                    ans = path[:]
                return

            solve(idx + 1, prev, path)

            if prev == -1 or nums[idx] % nums[prev] == 0:
                path.append(nums[idx])
                solve(idx + 1, idx, path)
                path.pop()

        solve(0, -1, [])
        return ans