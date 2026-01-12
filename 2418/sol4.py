class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        indices = list(range(len(names)))
        indices.sort(key=lambda i: heights[i], reverse=True)
        return [names[i] for i in indices]
