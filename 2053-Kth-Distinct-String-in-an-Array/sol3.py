class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for w in arr:
            freq[w] = freq.get(w, 0) + 1

        cnt = 0
        for w in arr:
            if freq[w] == 1:
                cnt += 1
                if cnt == k:
                    return w
        return ""
