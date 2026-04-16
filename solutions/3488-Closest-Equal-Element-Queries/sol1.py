class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for num in queries:
            temp = float("inf")

            for i in range(n):
                if nums[i] == nums[num] and i != num:
                    dist = min(abs(num - i), n - abs(num - i))
                    temp = min(temp, dist)

            if temp == float("inf"):
                temp = -1

            ans.append(temp)

        return ans