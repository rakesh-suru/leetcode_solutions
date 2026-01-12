class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = "a"
        while len(ans) <= k:
            for w in ans:
                temp = ord(w) + 1
                ans += chr(temp)
        print(ans)
        return ans[k-1]