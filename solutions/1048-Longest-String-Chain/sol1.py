class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)

        @lru_cache
        def dfs(word):
            ans = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in word_set:
                    ans = max(ans, 1 + dfs(prev))

            return ans

        return max(dfs(word) for word in words)