class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)
        
        if endWord not in words:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == endWord:
                return steps
            
            for i in range(len(curr)):
                for j in range(26):
                    temp = curr[:i] + chr(ord('a') + j) + curr[i+1:]
                    
                    if temp in words:
                        queue.append((temp, steps + 1))
                        words.remove(temp)
        
        return 0