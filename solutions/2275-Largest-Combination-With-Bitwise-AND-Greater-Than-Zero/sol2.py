class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0

        for bit in range(32):
            count = 0

            for num in candidates:
                if num & (1 << bit):
                    count += 1

            ans = max(ans, count)

        return ans