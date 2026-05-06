class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        mapper = Counter(moves)
        return abs(mapper['L'] - mapper['R']) + mapper['_']