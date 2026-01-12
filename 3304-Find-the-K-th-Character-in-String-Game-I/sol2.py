class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = ['a']

        while len(ans) < k:
            for i in range(len(ans)):
                next_ch = chr(ord("a") + ((ord(ans[i]) - ord("a") + 1) % 26))
                ans.append(next_ch)
        
        return ans[k-1]