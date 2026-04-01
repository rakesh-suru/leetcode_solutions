class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots = [[p, h, d, i] for p, h, d, i in robots]
        robots.sort(key=lambda x: x[0])

        stack = []
        idx = 0
        
        while idx < len(positions):

            if not stack:
                stack.append(robots[idx])
                idx += 1
                continue
            
            curr = stack[-1]

            if curr[2] == 'R' and robots[idx][2] == 'L':

                if curr[1] == robots[idx][1]:
                    stack.pop()
                    idx += 1

                elif curr[1] < robots[idx][1]:
                    robots[idx][1] -= 1
                    stack.pop()

                else:
                    stack[-1][1] -= 1
                    idx += 1

            else:
                stack.append(robots[idx])
                idx += 1
        
        res = [0] * len(positions)
        for robot in stack:
            res[robot[3]] = robot[1]

        return [x for x in res if x > 0]