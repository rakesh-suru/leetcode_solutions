class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        ans = []
        while any(freq.values()):
            row = []
            for num in list(freq.keys()):
                if freq[num] > 0:
                    row.append(num)
                    freq[num] -= 1
            ans.append(row)
        return ans
