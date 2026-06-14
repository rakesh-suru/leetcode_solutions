class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        temp = []
        n = len(nums)

        for i in range(n):
            maxi = nums[i]
            mini = nums[i]

            for j in range(i, n):
                maxi = max(maxi, nums[j])
                mini = min(mini, nums[j])

                temp.append(maxi - mini)

        temp.sort(reverse=True)

        return sum(temp[:k])