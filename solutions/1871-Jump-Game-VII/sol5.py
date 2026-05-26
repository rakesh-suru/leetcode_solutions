class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        q = deque([0])
        farthest = 0

        while q:
            idx = q.popleft()

            if idx == n - 1:
                return True

            left = max(idx + minJump, farthest + 1)
            right = min(idx + maxJump, n - 1)

            for i in range(left, right + 1):
                if s[i] == "0":
                    q.append(i)

            farthest = right

        return False