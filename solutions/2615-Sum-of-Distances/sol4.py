class Solution:
    def distance(self, nums):
        mapper = defaultdict(list)

        for i, num in enumerate(nums):
            mapper[num].append(i)
        
        ans = [0] * len(nums)
        
        for indices in mapper.values():
            total = sum(indices)
            left_sum = 0
            k = len(indices)
            
            for i, idx in enumerate(indices):
                right_sum = total - left_sum - idx

                left_count = i
                right_count = k - i - 1

                ans[idx] = (idx * left_count - left_sum) + (right_sum - idx * right_count)

                left_sum += idx
        
        return ans