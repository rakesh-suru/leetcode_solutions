class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = "nesw"
        curr_dir = 0
        curr = [0, 0]
        obstacles = set(map(tuple, obstacles))
        max_dist = 0

        for cmd in commands:
            if cmd == -1:
                curr_dir = (curr_dir + 1) % 4

            elif cmd == -2:
                curr_dir = (curr_dir - 1) % 4
            
            else:
                if directions[curr_dir] == "n":
                    for i in range(cmd):
                        curr[1] += 1
                        if tuple(curr) in obstacles:
                            curr[1] -= 1
                            break
                    max_dist = max(max_dist, curr[0]**2 + curr[1]**2)
                
                elif directions[curr_dir] == "s":
                    for i in range(cmd):
                        curr[1] -= 1
                        if tuple(curr) in obstacles:
                            curr[1] += 1
                            break
                    max_dist = max(max_dist, curr[0]**2 + curr[1]**2)
                
                elif directions[curr_dir] == "e":
                    for i in range(cmd):
                        curr[0] += 1
                        if tuple(curr) in obstacles:
                            curr[0] -= 1
                            break
                    max_dist = max(max_dist, curr[0]**2 + curr[1]**2)
                
                else:
                    for i in range(cmd):
                        curr[0] -= 1
                        if tuple(curr) in obstacles:
                            curr[0] += 1
                            break
                    max_dist = max(max_dist, curr[0]**2 + curr[1]**2)
        
        return max_dist