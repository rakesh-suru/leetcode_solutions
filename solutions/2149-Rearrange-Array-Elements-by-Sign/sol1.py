class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        ans = []
        i = 0
        while i < len(pos):
            ans.append(pos[i])
            ans.append(neg[i])
            i += 1
        return ans