class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        for q in queries:
            indices = pos[nums[q]]

            if len(indices) == 1:
                ans.append(-1)
                continue

            i = bisect.bisect_left(indices, q)

            temp = float("inf")

            left = indices[i - 1] if i > 0 else indices[-1]
            dist = min(abs(q - left), n - abs(q - left))
            temp = min(temp, dist)

            right = indices[i + 1] if i < len(indices) - 1 else indices[0]
            dist = min(abs(q - right), n - abs(q - right))
            temp = min(temp, dist)

            ans.append(temp)

        return ans