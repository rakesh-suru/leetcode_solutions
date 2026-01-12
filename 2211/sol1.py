class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0

        for car in directions:
            while stack:
                top = stack[-1]

                if top == 'R' and car == 'L':
                    collisions += 2
                    stack.pop()
                    car = 'S'

                elif top == 'R' and car == 'S':
                    collisions += 1
                    stack.pop()
                    car = 'S'

                elif top == 'S' and car == 'L':
                    collisions += 1
                    car = 'S'

                else:
                    break

            stack.append(car)

        return collisions
