class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mapper = {}
        for idx, num in enumerate(nums):
            if num not in mapper:
                mapper[num] = [idx]
            else:
                mapper[num].append(idx)
        
        ans = float("inf")
        found = False
        for key in mapper.keys():
            if len(mapper[key]) >= 3:
                found = True
                for i in range(0, len(mapper[key]) - 2):
                    mini = mapper[key][i]
                    maxi = mapper[key][i + 2]
                    ans = min(ans, 2 * (maxi - mini))
        
        if found:
            return ans
        return -1