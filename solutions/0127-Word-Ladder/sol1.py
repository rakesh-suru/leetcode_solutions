class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ans = 0
        queue = deque()
        words = set(wordList)

        if beginWord == endWord or endWord not in words:
            return ans
        
        queue.append((beginWord, 1))

        while queue:
            curr, val = queue.popleft()
            if curr == endWord:
                ans = val
                break

            for i in range(len(curr)):
                for j in range(26):
                    temp = curr[:i] + chr(ord("a") + j) + curr[i + 1:]
                    if temp in words:
                        queue.append((temp, val + 1))
                        words.remove(temp)
        
        return ans