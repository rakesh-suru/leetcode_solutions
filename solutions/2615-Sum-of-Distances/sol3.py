class Solution:
    def distance(self, nums):
        mapper = defaultdict(list)
        
        for i, num in enumerate(nums):
            mapper[num].append(i)
        
        n = len(nums)
        ans = [0] * n
        
        for indices in mapper.values():
            prefix = [0]
            
            for idx in indices:
                prefix.append(prefix[-1] + idx)
            
            k = len(indices)
            
            for i in range(k):
                idx = indices[i]
                
                left = i * idx - prefix[i]
                right = (prefix[k] - prefix[i+1]) - (k - i - 1) * idx
                
                ans[idx] = left + right
        
        return ans