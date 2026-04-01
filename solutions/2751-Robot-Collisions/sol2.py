class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots.sort()

        stack = []

        for pos, health, direction, idx in robots:

            if direction == 'R':
                stack.append([health, direction, idx])
            else:
                while stack and stack[-1][1] == 'R' and health > 0:
                    if stack[-1][0] < health:
                        health -= 1
                        stack.pop()
                    elif stack[-1][0] == health:
                        stack.pop()
                        health = 0
                    else:
                        stack[-1][0] -= 1
                        health = 0

                if health > 0:
                    stack.append([health, direction, idx])

        res = [0] * len(positions)
        for health, _, idx in stack:
            res[idx] = health

        return [x for x in res if x > 0]