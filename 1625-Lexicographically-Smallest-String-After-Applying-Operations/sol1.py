class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        def a_op(temp, a):
            temp = list(temp)
            for i in range(1, len(temp), 2):
                temp[i] = str((int(temp[i]) + a) % 10)
            return ''.join(temp)
        
        def b_op(temp, b):
            b = b % len(temp)
            return temp[-b:] + temp[:-b]
        
        seen = set()
        queue = deque([s])
        ans = s

        while queue:
            curr = queue.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            if curr < ans:
                ans = curr

            added = a_op(curr, a)
            rotated = b_op(curr, b)

            if added not in seen:
                queue.append(added)
            if rotated not in seen:
                queue.append(rotated)

        return ans