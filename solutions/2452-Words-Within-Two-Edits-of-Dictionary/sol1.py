class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        
        for query in queries:
            for word in dictionary:
                diff = 0
                
                for i in range(len(query)):
                    if query[i] != word[i]:
                        diff += 1
                    if diff > 2:
                        break
                
                if diff <= 2:
                    ans.append(query)
                    break
        
        return ans