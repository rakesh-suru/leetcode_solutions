class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        mapper = Counter(moves)

        if mapper["L"] == mapper["R"]:
            return mapper["_"]

        elif mapper["L"] > mapper["R"]:
            return mapper["L"] + mapper["_"] - mapper["R"]
        
        else:
            return mapper["R"] + mapper["_"] - mapper["L"]