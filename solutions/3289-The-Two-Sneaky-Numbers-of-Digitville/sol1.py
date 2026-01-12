class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        visited = []
        for num in nums:
            if num not in visited:
                visited.append(num)
            else:
                ans.append(num)
        return ans