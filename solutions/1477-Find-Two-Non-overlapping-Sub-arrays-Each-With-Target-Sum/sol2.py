class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        best = [float('inf')] * (n + 1)

        ans = float('inf')

        for r in range(n):
            best[r + 1] = best[r]

            for l in range(r + 1):
                curr_sum = prefix[r + 1] - prefix[l]

                if curr_sum == target:
                    length = r - l + 1

                    if best[l] != float('inf'):
                        ans = min(ans, length + best[l])

                    best[r + 1] = min(best[r + 1], length)

        return -1 if ans == float('inf') else ans