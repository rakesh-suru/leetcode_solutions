class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        ans = []

        for num in nums:
            if freq[num] >= len(ans):
                ans.append([])
            
            ans[freq[num]].append(num)
            freq[num] += 1
        
        return ans