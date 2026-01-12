class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        ans = 0
        for num in nums:
            tmp, tmp2 = num - k, num + k
            if tmp in seen:
                ans += seen[tmp]
            if tmp2 in seen:
                ans += seen[tmp2]
            
            seen[num] += 1
        
        return ans