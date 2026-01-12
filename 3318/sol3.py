class Solution:
    def findXSum(self, nums, k, x):
        ans = []
        for i in range(len(nums) - k + 1):
            subarr = nums[i:i+k]
            cnt = Counter(subarr)
            temp = [[num, cnt[num]] for num in cnt]
            temp.sort(key=lambda x: (-x[1], -x[0]))
            total = 0
            for j in range(min(x, len(temp))):
                total += temp[j][0] * temp[j][1]
            ans.append(total)
        return ans
