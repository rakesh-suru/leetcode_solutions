class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            subarr = nums[i : i + k]
            cnt = Counter(subarr)
            temp = []

            for num in cnt:
                temp.append([num, cnt[num]])
            temp.sort(key = lambda x : (-x[1], -x[0]))
            tempsum = 0

            for i in range(min(x, len(temp))):
                tempsum += temp[i][0] * temp[i][1]
            ans.append(tempsum)
        return ans