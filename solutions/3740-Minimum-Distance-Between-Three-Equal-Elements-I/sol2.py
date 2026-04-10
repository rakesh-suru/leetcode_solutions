class Solution:
    def minimumDistance(self, nums: List[int]) -> int:       
        mapper = defaultdict(list)
        
        for i, num in enumerate(nums):
            mapper[num].append(i)
        
        ans = float("inf")
        
        for indices in mapper.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    ans = min(ans, 2 * (indices[i+2] - indices[i]))
        
        return ans if ans != float("inf") else -1