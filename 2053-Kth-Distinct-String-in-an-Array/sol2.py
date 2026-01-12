class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        cnt = 0

        for word in arr:
            if freq[word] == 1:
                cnt += 1
                if cnt == k:
                    return word
        return ""
