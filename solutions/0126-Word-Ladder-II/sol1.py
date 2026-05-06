class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
       
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        queue = deque()
        queue.append([beginWord])
        
        res = []
        found = False
        
        while queue and not found:
            visited_this_level = set()
            
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
                            visited_this_level.add(temp)
            
            wordSet -= visited_this_level
        
        return res