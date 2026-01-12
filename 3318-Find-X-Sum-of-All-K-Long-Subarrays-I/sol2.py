class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            cnt = Counter(nums[i:i+k])

            if len(cnt) <= x:
                ans.append(sum(nums[i:i+k])) 
            else:
                pairs = list(cnt.items())
                pairs.sort(key = lambda p: (p[1], p[0]), reverse = True)
                curr_sum = 0
                for num, cnt in pairs[:x]:
                    curr_sum += (num * cnt)
                ans.append(curr_sum)
        return ans