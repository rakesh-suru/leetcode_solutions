from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        parents = defaultdict(list)
        level = {beginWord}
        
        while level and endWord not in parents:
            next_level = defaultdict(list)
            
            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue
                        
                        temp = word[:i] + c + word[i+1:]
                        
                        if temp in wordSet:
                            next_level[temp].append(word)
            
            wordSet -= set(next_level.keys())
            level = next_level
            
            for word in next_level:
                parents[word].extend(next_level[word])
        
        res = []
        
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for parent in parents[word]:
                dfs(parent, path + [parent])
        
        if endWord in parents:
            dfs(endWord, [endWord])
        
        return res