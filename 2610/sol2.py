class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = [[nums[0]]]
        for num in nums[1:]:
            placed = False
            for row in ans:
                if num not in row:
                    row.append(num)
                    placed = True
                    break
            if not placed:
                ans.append([num])
        return ans
