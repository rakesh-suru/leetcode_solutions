class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        ans = [name for _, name in sorted(zip(heights, names), reverse=True)]
        return ans