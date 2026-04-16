class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        for num in queries:
            temp = float("inf")

            for i in pos[nums[num]]:
                if i != num:
                    dist = min(abs(num - i), n - abs(num - i))
                    temp = min(temp, dist)

            if temp == float("inf"):
                temp = -1
            
            ans.append(temp)

        return ans