class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        
        for q in queries:
            for w in dictionary:
                if sum(q[i] != w[i] for i in range(len(q))) <= 2:
                    ans.append(q)
                    break
        
        return ans