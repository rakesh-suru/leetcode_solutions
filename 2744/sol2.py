class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        visited = [False] * n
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if not visited[i] and not visited[j] and words[i] == words[j][::-1]:
                    ans += 1
                    visited[i] = visited[j] = True
        return ans
