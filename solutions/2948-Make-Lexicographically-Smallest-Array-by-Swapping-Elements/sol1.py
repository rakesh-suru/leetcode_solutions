class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        pairs = [(nums[i], i) for i in range(n)]
        pairs.sort()

        result = nums[:]
        start = 0

        while start < n:
            end = start

            while end + 1 < n and pairs[end + 1][0] -  pairs[end][0] <= limit:
                end += 1
            
            val = []
            idx = []

            for i in range(start, end + 1):
                val.append(pairs[i][0])
                idx.append(pairs[i][1])
            
            idx.sort()

            for i in range(len(idx)):
                result[idx[i]] = val[i]
            

            start = end + 1
        
        return result