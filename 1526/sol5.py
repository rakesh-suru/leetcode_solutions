class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        stack = [(0, 0)]

        for h in target:
            work = max(0, h - stack[-1][0])

            while stack and h >= stack[-1][0]:
                _, prev_work = stack.pop()
                operations += prev_work
            stack.append((h, work))
        
        while stack:
            operations += stack.pop()[1]
        
        return operations