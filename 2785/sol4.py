class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        heap = [ch for ch in s if ch in vowels]
        heapq.heapify(heap)

        ans = []
        for ch in s:
            if ch in vowels:
                ans.append(heapq.heappop(heap))
            else:
                ans.append(ch)
        return "".join(ans)
