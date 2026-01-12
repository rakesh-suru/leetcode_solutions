class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        seen = set()
        queue = deque([s])
        ans = s

        while queue:
            curr = queue.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            ans = min(ans, curr)

            chars = list(curr)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)

            rotated = curr[-b:] + curr[:-b]

            queue.append(added)
            queue.append(rotated)

        return ans
