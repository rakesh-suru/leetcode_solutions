class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0

        while i < len(asteroids):
            if not stack or asteroids[i] > 0 or stack[-1] < 0:
                stack.append(asteroids[i])
                i += 1
            
            else:
                if abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    i += 1
                else:
                    i += 1
        
        return stack