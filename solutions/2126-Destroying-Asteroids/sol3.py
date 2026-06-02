import heapq

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapq.heapify(asteroids)

        while asteroids:
            ast = heapq.heappop(asteroids)

            if ast > mass:
                return False

            mass += ast

        return True