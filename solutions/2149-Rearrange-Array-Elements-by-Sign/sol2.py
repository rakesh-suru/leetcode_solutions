class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, ans = [], [], []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        
        i = 0
        while i < len(pos):
            ans.append(pos[i])
            ans.append(neg[i])
            i += 1
        return ans