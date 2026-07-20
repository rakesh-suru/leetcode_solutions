class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(arr)
        ranks = []
        rank = 0
        curr = -float("inf")

        for num in temp:
            if num > curr:
                rank += 1
            ranks.append(rank)
            curr = num
        
        mapper = {}
        for i in range(len(temp)):
            mapper[temp[i]] = ranks[i]
        
        ans = []
        for num in arr:
            ans.append(mapper[num])
        
        return ans