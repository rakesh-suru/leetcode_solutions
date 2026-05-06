class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        queue = deque([[beginWord]])
        res = []
        
        found = False
        visited = set()
        
        while queue and not found:
            level_visited = set()
            
            for _ in range(len(queue)):
                path = queue.popleft()
                word = path[-1]
                
                if word == endWord:
                    res.append(path)
                    found = True
                    continue
                
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        temp = word[:i] + c + word[i+1:]
                        
                        if temp in wordSet:
                            queue.append(path + [temp])
                            level_visited.add(temp)

            wordSet -= level_visited
        
        return res