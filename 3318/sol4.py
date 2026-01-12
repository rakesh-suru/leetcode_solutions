class Solution:
    def findXSum(self, nums, k, x):
        ans = []
        freq = Counter(nums[:k])
        for i in range(len(nums) - k + 1):
            temp = [[num, freq[num]] for num in freq]
            temp.sort(key=lambda x: (-x[1], -x[0]))
            total = sum(temp[j][0]*temp[j][1] for j in range(min(x, len(temp))))
            ans.append(total)
            
            if i + k < len(nums):
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
                freq[nums[i+k]] += 1
        return ans