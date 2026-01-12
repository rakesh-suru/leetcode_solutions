class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        mapping = dict(zip(heights, names))
        
        heights.sort(reverse=True)
        
        return [mapping[h] for h in heights]
