class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        visited = [0] * n
        for i in range(n-1):
            for j in range(i+1,n):
                if words[i] == words[j][::-1] and not visited[i] and not visited[j]:
                    ans += 1
                    visited[i] = 1
                    visited[j] = 1
        return ans