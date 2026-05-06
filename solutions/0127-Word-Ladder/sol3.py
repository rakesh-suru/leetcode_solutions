class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        beginSet = {beginWord}
        endSet = {endWord}
        
        steps = 1
        
        while beginSet and endSet:

            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            nextSet = set()
            
            for word in beginSet:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        temp = word[:i] + c + word[i+1:]
                        
                        if temp in endSet:
                            return steps + 1
                        
                        if temp in wordSet:
                            nextSet.add(temp)
                            wordSet.remove(temp)
            
            beginSet = nextSet
            steps += 1
        
        return 0