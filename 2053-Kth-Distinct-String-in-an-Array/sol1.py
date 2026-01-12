class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = []
        for word in arr:
            if arr.count(word) == 1:
                ans.append(word)
        return ans[k-1] if k <= len(ans) else ""