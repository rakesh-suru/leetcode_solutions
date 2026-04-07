class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x = y = 0
        dir = 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:
                dir = (dir + 1) % 4
            elif cmd == -2:
                dir = (dir - 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    
                    if (nx, ny) in obs:
                        break
                    
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist